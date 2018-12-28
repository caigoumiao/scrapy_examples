# -*- coding: utf-8 -*-
import scrapy


class ShiwenSpider(scrapy.Spider):
    name = 'shiwen'
    allowed_domains = ['https://www.gushiwen.org/shiwen/']
    start_urls = ['https://www.gushiwen.org/shiwen//']

    def parse(self, response):
        filename=response.url.split('/')[-2]+".html"
        with open(filename, 'wb') as fp:
            fp.write(response.body)
