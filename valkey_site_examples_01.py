# https://github.com/valkey-io/valkey-py
import valkey
r = valkey.Valkey(host='localhost', port=6379, db=0)
print(r.set('foo', 'bar'))
# True
print(r.get('foo'))
# b'bar'
