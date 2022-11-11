# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazondatascrapingItem(scrapy.Item):
    # define the fields for your item here like:
    item_title = scrapy.Field()
    item_author = scrapy.Field()
    item_price= scrapy.Field()
    item_image = scrapy.Field()
    item_link= scrapy.Field()
    
