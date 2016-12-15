from pykafka import KafkaClient

def consume_msg(ip_address, k_topic):
    client = KafkaClient(hosts=ip_address)
    topic = client.topics[str.encode(k_topic)]

    consumer = topic.get_simple_consumer(consumer_timeout_ms=5000)
    for msg in consumer:
        print(msg.value, msg.partition_key, msg.partition_id, msg.offset)
