# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field, Item


class PostloopItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    user_name = Field()
