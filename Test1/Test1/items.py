# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Test1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Username = scrapy.Field()
    Fullname = scrapy.Field()
    Followers = scrapy.Field()
    Following =scrapy.Field()
    Biography = scrapy.Field()
    Private =  scrapy.Field()
    Verify =   scrapy.Field()
    Noposts =  scrapy.Field()
    Liked  = scrapy.Field()
    comment = scrapy.Field()
