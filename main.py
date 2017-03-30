import redis, os

r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=6379, db=0)

pubsub = r.pubsub()
pubsub.psubscribe('*')

containers = {}

for msg in pubsub.listen():
  print msg
  if msg['type'] == 'pmessage':
    containers[msg['channel']] = int(msg['data'])
    print(containers)
