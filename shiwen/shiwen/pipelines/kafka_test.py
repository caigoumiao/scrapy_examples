from kafka.producer import KafkaProducer


def send_demo():
    producer=KafkaProducer(bootstrap_servers='172.18.100.90:9092')
    producer.send('send_demo',b'some messages bytes')


if __name__ == '__main__':
    send_demo()