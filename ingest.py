import sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h:t:r:", ["test=","run="])
    except getopt.GetoptError:
        print("ingest.py -t <test_string> -r <run_command>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-t", "--test"):
            print(arg)
        elif opt in ("-r", "--run"):
            # TODO: add ipaddress and topic as args could also be global
            if arg == "producer":
                producer()
            else:
                consumer()

def producer():
    import producer
    # TODO: set 9092 as default and add to ip_address
    # producer.produce_msg("172.17.0.3" + ":9092", "tps")
    producer.start_stream()

def consumer():
    import consumer
    consumer.consume_msg("172.17.0.3"  + ":9092", "test1")

if __name__ == '__main__':
    main(sys.argv[1:])
