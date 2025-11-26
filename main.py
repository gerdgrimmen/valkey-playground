from valkey import Valkey

val = Valkey(host="localhost", port=6379, db=0)
val.set("name", "me")
value = val.get("name")
print(value)
