# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
from tinydb import TinyDB, Query
from benckebot.mailmanager import sendmail


class BenckePipeline(object):

    def open_spider(self, spider):
        self.db = TinyDB('benckebot/benckeDB.json')

    def close_spider(self, spider):
        searcher = Query()
        listOfApartments = self.db.search((searcher.isBuyable == True) & (searcher.isNew == True))
        if len(listOfApartments) > 0:
            sendmail(listOfApartments)
        self.db.update({'isNew': False}, searcher.isNew == True)

    def process_item(self, item, spider):
        searcher = Query()
        isNew = False
        isBuyable = False

        tempshah = hashlib.sha256(bytes(item["id"] + item["url"] + str(item["zipCode"]), "utf8")).hexdigest()
        if len(self.db.search(searcher.uid == tempshah)) > 0:
            return item

        isNew = True

        if int(item["zipCode"]) <= 2650 and int(item["price"]) <= 1200000 and int(item["expenses"]) <= 4500:
            isBuyable = True

        self.db.insert({'description': item["id"],
                        'price': item["price"],
                        'expenses': item["expenses"],
                        'url': item["url"],
                        'zipCode': item["zipCode"],
                        'uid': tempshah,
                        'isNew': isNew,
                        'isBuyable': isBuyable})

        return item
