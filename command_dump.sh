
# https://www.youtube.com/watch?v=IRli5I9MxOs
keys * 

set key value
set name jesse
get name
# jesse
# 3:35
# Valkey.from_url("valkey:://localhost:6379")
# r.ping()
# pool = ConnectionPool(host=localhost, port=6379, db=0)
# r = Valkey(connection_pool=pool)
# 8:50
r.set("name", "me")
value = r.get("name")
exists = r.exists("name")
print(exists)
# 1

# 10:40
# expiration - ttl in seconds
r.expire("name", 60)

r.incr("counter")
r.decr("counter")

# 13:10
r.set("category", "languages")
r.append("category", "books") # string append
r.get("category")

# 14:10