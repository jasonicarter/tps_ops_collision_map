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
            if arg == "producer":
                producer() # TODO: add ipaddress and topic
            else:
                consumer()

def producer():
    import producer
    # import tweets
    producer.producer_init("IPAddress", "tps_ops")
    producer.produce_msg() # tweets.start_stream

def consumer():
    import consumer
    consumer.consumer_say_hello()

if __name__ == '__main__':
    main(sys.argv[1:])
