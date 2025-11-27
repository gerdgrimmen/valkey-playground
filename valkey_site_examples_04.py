# https://github.com/valkey-io/valkey-py
import valkey as redis
r = redis.Redis(host='localhost', port=6379, db=0)

r = valkey.Valkey(...)
p = r.pubsub()
p.subscribe('my-first-channel', 'my-second-channel', ...)
p.get_message()
{'pattern': None, 'type': 'subscribe', 'channel': b'my-second-channel', 'data': 1}