# dockercon-monitor
A Raspberry Pi based monitor for the [Swarm](https://github.com/developius/dockercon-swarm-app/)!

## Running

### .env file
Create a `.env` file in the current directory with these lines, then save & close it:

```
REDIS_HOST=<redis host>
REDIS_PASSWD=<redis password>
```

`docker run -ti --rm --privileged --device /dev/gpiomem:/dev/gpiomem --env-file .env developius/swarm-app-monitor:latest`

_Note: requires a running redis instance at `<redis host>` with password `<redis password>`_

## Building (optional)

`docker build -t developius/swarm-app-monitor .`
