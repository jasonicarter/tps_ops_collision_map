# A Toronto Collision Map
A Toronto traffic collision map based on tweets by TPS Operations.

## A Data Engineering Effort

## Setup

1. Install [Docker](https://www.docker.com/)
2. TODO: [Docker-Compose](https://docs.docker.com/compose/)

## Usage

1. Lets start everything up...

[Optional] Make sure nothing is running or names are not in use by other containers
- List all running processes `docker ps` and `docker stop [container]` if running
- Delete all containers `docker rm $(docker ps -a -q)`
- Delete all images `docker rmi $(docker images -q)`

Apache Zookeeper is a must for running a Kafka and Storm. Since the Zookeeper "fails fast" it's better to always restart it.

```bash
docker run -d --restart always --name zookeeper zookeeper:3.4
docker run -d --restart always --name kafka --link zookeeper:zookeeper ches/kafka
docker run -d --restart always --name nimbus --link zookeeper:zookeeper storm:1.0.2 storm nimbus
docker run -d --restart always --name supervisor --link zookeeper:zookeeper --link nimbus:nimbus storm:1.0.2 storm supervisor

# optionally, start the Storm UI
docker run -d -p 8080:8080 --restart always --name ui --link nimbus:nimbus storm:1.0.2 storm ui
```
`--link` is [deprecated](https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/)
need to stick this into Docker Compose

2. Get ip address (TODO: make this process simpler)

```bash
ZK_IP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' zookeeper)
KAFKA_IP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' kafka)
echo $ZK_IP, $KAFKA_IP
```

3. Create Kafka topic

```bash
docker run --rm ches/kafka kafka-topics.sh --create --topic test --replication-factor 1 --partitions 1 --zookeeper $ZK_IP:2181
```
Output should show `Created topic "test".` For the list of topics: `docker run --rm ches/kafka kafka-topics.sh --list --zookeeper $ZK_IP:2181`

4. Test out Kafka

In separate terminals:
```bash
docker run --rm --interactive ches/kafka kafka-console-producer.sh --topic test --broker-list $KAFKA_IP:9092
<type messages followed by newline>
```

Repeat step 2 (new terminal wont have $ZK_IP or $KAFKA_IP variables):
```bash
docker run --rm ches/kafka kafka-console-consumer.sh --topic test --from-beginning --zookeeper $ZK_IP:2181
```
`--zookeeper` warning message: Using the ConsoleConsumer with old consumer is deprecated.
Consider using the new consumer by passing [bootstrap-server] instead of [zookeeper]

5. Build ```ingest.py``` and run ```producer``` and ```consumer``` in separate terminals

Building Python environment with pykafka and tweepy
```bash
docker build -t ingest .
```
Then run both `docker run ingest -r producer [consumer]` in separate terminals.
TODO: need to setup tweepy and testing
