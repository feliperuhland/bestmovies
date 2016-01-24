# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BestmoviesItem(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    rating = scrapy.Field()
    url = scrapy.Field()
    genres = scrapy.Field()
    director = scrapy.Field()
    stars = scrapy.Field()
