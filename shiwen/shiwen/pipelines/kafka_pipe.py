from kafka.producer import KafkaProducer
import json


class KafkaPipeline(object):
    kafka_uri = "172.18.100.90:9092"
    kafka_topic = "crapy_data"

    def __int__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=self.kafka_uri,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def process_item(self, item, spider):
        self.producer.send(self.kafka_topic, item)

    def close_spider(self, spider):
        self.producer.close()
