# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class StackPipeline(object):
#     def process_item(self, item, spider):
#         return item

import pymongo

from scrapy.utils.project import get_project_settings
settings = get_project_settings()
# Use the settings

from scrapy.exceptions import DropItem
import logging 

class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def print_dict(self, d):
        new = {}
        for k, v in d.items():
            if k.startswith('dc'):
                new[k.replace('.', '-')] = v
            else:
                new[k] = v
        return new

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Missing data!")

        item = self.print_dict(item)
        self.collection.update({'uri': item['dc-identifier-uri']}, dict(item), upsert=True)
        logging.debug("TFG added to MongoDB database!")
        return item

# class AddiPipeline(object):
#    def process_item(self, item, spider):
#        return item
