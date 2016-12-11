# A Toronto Collision Map
A Toronto traffic collision map based on tweets by TPS Operations.

## A Data Engineering Effort

## Setup

1. Install [Docker](https://www.docker.com/)
2. TODO: [Docker-Compose](https://docs.docker.com/compose/)

## Usage

1. Start up both Zookeeper and Kafka

```bash
docker run -d -p 2181:2181 --name zookeeper jplock/zookeeper
docker run -d --name kafka --link zookeeper:zookeeper ches/kafka
```
`--link` is [deprecated](https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/)

2. Build ```ingest.py``` and run ```producer``` and ```consumer```

Building Python environment with pykafka
```bash
docker build -t ingest .
```
Run a few tests: ` docker run ingest -t "hello world" ` should give you `hello world` back

And `docker run ingest -r producer [consumer]` should give you `hello world, from producer [consumer]`
