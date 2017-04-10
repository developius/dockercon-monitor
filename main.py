# -*- coding: utf-8 -*-
import gpiozero, redis, os, math, datetime
from gpiozero import AngularServo
import time

r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=6379, db=0, password=os.environ['REDIS_PASSWD'])
pubsub = r.pubsub()
pubsub.psubscribe('*')

used_containers = []
containers = {}

left = AngularServo(18, min_angle = 180, max_angle = 0, min_pulse_width=0.7/1000, max_pulse_width=2.3/1000)
right = AngularServo(12, min_angle = 180, max_angle = 0, min_pulse_width=0.7/1000, max_pulse_width=2.3/1000)

left.mid()
right.mid()
left.detach()
right.detach()
time.sleep(10)

def translate(value):
  valueScaled = value / 8.0 # highest value we'll get from log(reqs) (touchwood)
  valueScaled = valueScaled * 180
  if valueScaled > 146: return 146
  if valueScaled < 34: return 36
  return valueScaled

for msg in pubsub.listen():
  if msg['type'] == 'pmessage':
    container = msg['channel']
    reqs = int(msg['data'])
    if container in containers: containers[container]['reqs'] = reqs
    else:
      if 'right' not in used_containers:
        containers[container] = {
          'servo': right,
          'servo_name': 'right',
          'reqs': reqs,
          'lastseen': datetime.datetime.now()
          }
        used_containers.append('right')
      elif 'left' not in used_containers:
        containers[container] = {
          'servo': left,
          'servo_name': 'left',
          'reqs': reqs,
          'lastseen': datetime.datetime.now()
        }
        used_containers.append('left')
      else:
        print('Could not assign a servo to container {}, they are all in use'.format(container))
        continue # move on with messages

    angle = 0
    if reqs > 0: angle = math.log(reqs)
    angle = translate(angle)
    containers[container]['servo'].angle = angle
    containers[container]['lastseen'] = datetime.datetime.now()

    for key in containers.keys():
      if containers[key]['lastseen'] < datetime.datetime.now() - datetime.timedelta(seconds=3): # 3 missed updates
        print('Removing container {} as it\'s been unresponsive for 3s'.format(key))
        used_containers.remove(containers[key]['servo_name']) # make the servo available again
        containers.pop(key, None) # remove the container

    output = []
    for container, data in containers.iteritems():
      output.append('{}: {}º ({} req/s)'.format(container, data['servo'].angle, data['reqs']))
    print(', '.join(output))
