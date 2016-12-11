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
                producer()
            else:
                consumer()

def producer():
    import producer
    producer.producer_say_hello()

def consumer():
    import consumer
    consumer.consumer_say_hello()

if __name__ == '__main__':
    main(sys.argv[1:])
