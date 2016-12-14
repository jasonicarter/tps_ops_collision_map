from pykafka import KafkaClient

def consume_msg(ip_address, k_topic):
    # TODO: set 9092 as default and add to ip_address
    client = KafkaClient(hosts='172.17.0.3:9092') #b'172.17.0.3:9092', b'tps_ops'
    topic = client.topics[b'tps_ops']

    consumer = topic.get_simple_consumer(consumer_timeout_ms=5000)
    for msg in consumer:
        print(msg)
        # print(
        #   ”%s [key=%s, id=%s, offset=%s]” %
        #   (msg.value, msg.partition_key, msg.partition_id, msg.offset))

def consumer_say_hello():
    print("Hello World, from Consumer")
