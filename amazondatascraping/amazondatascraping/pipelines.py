# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
# import items

class AmazondatascrapingPipeline:
    def __init__(self):
        self.client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=self.client["AmazonData"]
        self.client=db["Books"]
    def process_item(self, item, spider):
        self.client.insert_one(dict(item))
        return item
       
#jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjsssssssssssssssssssssssssss