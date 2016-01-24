# -*- coding: utf-8 -*-

import scrapy

from bestmovies.items import BestmoviesItem


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ['http://www.imdb.com/chart/top?ref_=nv_mv_250_6/']

    def parse(self, response):
        for movie_url in response.xpath('//td[@class="titleColumn"]/a/@href'):
            url = response.urljoin(movie_url.extract().split('?')[0])
            yield scrapy.Request(url, callback=self.parse_movie)

    def parse_movie(self, response):
        item = BestmoviesItem()
        item['name'] = response.xpath('//h1[@class="header"]/span[@itemprop="name"]/text()').extract_first()
        item['url'] = response.url
        item['year'] = response.xpath('//span[@class="nobr"]/a/text()').extract_first()
        item['rating'] = response.xpath('//span[@itemprop="ratingValue"]/text()').extract_first()
        item['genres'] = ';'.join([g.extract().strip() for g in response.xpath('//div[@itemprop="genre"]/a/text()')])
        item['director'] = response.xpath('//div[@itemprop="director"]/a/span/text()').extract_first()
        item['stars'] = ';'.join([a.extract() for a in response.xpath('//div[@itemprop="actors"]/a/span/text()')])
        yield item
