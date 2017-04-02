# dockercon-monitor
A Raspberry Pi based monitor for the [Swarm](https://github.com/developius/dockercon-swarm-app/)!

## Running

`docker run -ti --rm --privileged --device /dev/gpiomem:/dev/gpiomem --env REDIS_HOST=<redis host> --env REDIS_PASSWD=<redis passwd> developius/swarm-app-monitor:latest`

## Building (optional)

`docker build -t developius/swarm-app-monitor .`

_Note: requires a running redis instance at `<redis host>`_
