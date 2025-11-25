# https://github.com/valkey-io/valkey-py
docker run -p 6379:6379 -it valkey/valkey:latest

# not from website
podman run -d -p 6379:6379 -it docker.io/valkey/valkey:latest