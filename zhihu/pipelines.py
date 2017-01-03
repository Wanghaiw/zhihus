# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from zhihu.items import ZhihuItem
from scrapy.exceptions import DropItem





class ZhihuPipeline(object):


    def __init__(self):
        connection = pymongo.MongoClient()
        self.db = connection['zhihu']
        self.zh_user = self.db['zh_user']


    def process_item(self, item, spider):
        if isinstance(item,ZhihuItem):
            self.saveOrUpdate(self.zh_user,item)

    def saveOrUpdate(self,collection,item):

        try:
            collection.insert(dict(item))
            return item
        except:
            raise DropItem('重复咯')





