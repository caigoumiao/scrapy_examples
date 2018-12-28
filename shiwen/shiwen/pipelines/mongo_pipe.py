import pymongo


class MongoPipeline(object):
    collection_name = "shiwen"

    def __init__(self):
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
