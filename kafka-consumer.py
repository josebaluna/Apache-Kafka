from kafka import KafkaConsumer

def main():
    consumer = KafkaConsumer('bigdataroom', enable_auto_commit=False)
    for msg in consumer:
        #print(msg)  # print the total msg
        print(msg.value.decode())  # print the msg value


if __name__ == "__main__":
    main()
