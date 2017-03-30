# DockerCon Monitor
A Raspberry Pi based monitor for the Swarm, updating in real time!

## Running the monitor

`docker run --rm --env REDIS_HOST=<redis host> -ti developius/dockercon-monitor-armhf:latest`

_Note: requires a running redis instance at `<redis host>`_

## Building (optional)

`docker build -t developius/dockercon-monitor-armhf .`
