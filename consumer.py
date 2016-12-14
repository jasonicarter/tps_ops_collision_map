from pykafka import KafkaClient

def consume_msg():
    # TODO: need to pass in docker container ip and kafka topic
    client = KafkaClient("IPAddress:9092")
    topic = client.topics["tps_ops"]

    consumer = topic.get_simple_consumer(consumer_timeout_ms=5000)
    for msg in consumer:
        print(
          ”%s [key=%s, id=%s, offset=%s]” %
          (msg.value, msg.partition_key, msg.partition_id, msg.offset))

def consumer_say_hello():
    print("Hello World, from Consumer")
