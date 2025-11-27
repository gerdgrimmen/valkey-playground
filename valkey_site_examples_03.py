# https://github.com/valkey-io/valkey-py
import valkey as redis
r = redis.Redis(host='localhost', port=6379, db=0)

pipe = r.pipeline()

pipe.set('foo', 5)

pipe.set('bar', 18.5)

pipe.set('blee', "hello world!")

pipe.execute()
# [True, True, True]