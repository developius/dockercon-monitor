# -*- coding: utf-8 -*-
import gpiozero, redis, os, math
from gpiozero import AngularServo
from time import sleep

r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=6379, db=0, password=os.environ['REDIS_PASSWD'])
pubsub = r.pubsub()
pubsub.psubscribe('*')

used_containers = []
containers = {}

left = AngularServo(18, min_angle = 180, max_angle = 0, min_pulse_width=0.7/1000, max_pulse_width=2.3/1000)
right = AngularServo(12, min_angle = 180, max_angle = 0, min_pulse_width=0.7/1000, max_pulse_width=2.3/1000)

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
      if 'left' not in used_containers:
        containers[container] = { 'servo': left, 'reqs': reqs }
        used_containers.append('left')
      elif 'right' not in used_containers:
        containers[container] = { 'servo': right, 'reqs': reqs }
        used_containers.append('right')
      else: print('Could not assign a servo to container {}, they are all in use'.format(container))

    angle = 0
    if reqs > 0: angle = math.log(reqs)
    angle = translate(angle)
    containers[container]['servo'].angle = angle

    output = []
    for container, data in containers.iteritems():
      output.append('{}: {}º ({} req/s)'.format(container, data['servo'].angle, data['reqs']))
    print(', '.join(output))