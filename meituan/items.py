# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituanItem(scrapy.Item):
    name = scrapy.Field()
    score = scrapy.Field()
    avgPrice = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()

