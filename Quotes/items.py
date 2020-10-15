# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    quote = scrapy.Field()
    tags = scrapy.Field()
    author = scrapy.Field()
    author_link = scrapy.Field()
    
    pass
