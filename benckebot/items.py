# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BenckebotItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    zipCode = scrapy.Field()
    price = scrapy.Field()
    expenses = scrapy.Field()
