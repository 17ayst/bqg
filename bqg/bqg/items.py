# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BqgItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    ml=scrapy.Field()
    txt = scrapy.Field()
    pass
