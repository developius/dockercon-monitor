# dockercon-monitor
A Raspberry Pi based monitor for the Swarm!

## Running

`docker run -ti --rm --privileged --device /dev/gpiomem:/dev/gpiomem --env REDIS_HOST=<redis host> developius/swarm-app-monitor:latest`

## Building

`docker build -t developius/swarm-app-monitor .`