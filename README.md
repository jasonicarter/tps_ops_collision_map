# A Toronto Collision Map
A Toronto traffic collision map based on tweets by TPS Operations.

## A Data Engineering Effort

## Setup

1. Install [Docker](https://www.docker.com/)
2. TODO: [Docker-Compose](https://docs.docker.com/compose/)

## Usage

1. Start up both Zookeeper and Kafka

[Optional] Make sure nothing is running or names are not in use by other containers
- List all running processes `docker ps` and `docker stop [container]` if running
- Delete all containers `docker rm $(docker ps -a -q)`
- Delete all images `docker rmi $(docker images -q)`

```bash
docker run -d -p 2181:2181 --name zookeeper jplock/zookeeper
docker run -d --name kafka --link zookeeper:zookeeper ches/kafka
```
`--link` is [deprecated](https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/)

2. Get ip address (TODO: make this process simpler)

```bash
ZK_IP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' zookeeper)
KAFKA_IP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' kafka)
echo $ZK_IP, KAFKA_IP
```

3. Create Kafka topic

```bash
docker run --rm ches/kafka kafka-topics.sh --create --topic [test] --replication-factor 1 --partitions 1 --zookeeper $ZK_IP:2181
```

4. Build ```ingest.py``` and run ```producer``` and ```consumer``` in separate terminals

Building Python environment with pykafka and tweepy
```bash
docker build -t ingest .
```
Then run both `docker run ingest -r producer [consumer]` in separate terminals.
TODO: need to setup tweepy and testing
