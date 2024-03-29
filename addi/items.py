# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field 
from scrapy.loader.processors import MapCompose, TakeFirst

# import scrapy


class AddiItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    date = Field(
            input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    project = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    links = Field()
    repo = Field(
        # input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
