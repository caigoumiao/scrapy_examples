import pymongo
from kafka.producer import KafkaProducer
import json


# mongo 通道
class MongoPipeline(object):
    collection_name = "shiwen"

    def __init__(self):
        # todo 将配置项加到settings 文件中
        self.mongo_uri = '172.18.100.90'
        self.mongo_db = 'scrapy_data'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls{
    #         mongo_uri=crawler.settings.get('MONGO_URI'),
    #         mongo_db=crawler.settings.get('MONGO_DB')
    #     }

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item


# kafka 通道
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
