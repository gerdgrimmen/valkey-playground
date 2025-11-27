from valkey import Valkey

val = Valkey(host="localhost", port=6379, db=0)
val.set("name", "me")
value = val.get("name")
print(value)

val.delete("name")

val.hset("asd", "foo", "bar")

val.hset("asd", items=["asd",123])
values = val.hgetall("asd")
print(values)

values = val.hget("asd", "foo")
print(values)
