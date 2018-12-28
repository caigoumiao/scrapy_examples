from kafka.consumer import KafkaConsumer


def consumer_demo():
    consumer = KafkaConsumer('send_demo', group_id='g1', bootstrap_servers='172.18.100.90:9092')
    for msg in consumer:
        print(msg)


if __name__ == '__main__':
    consumer_demo()