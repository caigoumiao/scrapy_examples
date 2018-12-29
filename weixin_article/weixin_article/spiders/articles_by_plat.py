# -*- coding: utf-8 -*-
import scrapy


class ArticlesByPlatSpider(scrapy.Spider):
    name = 'articles_by_plat'
    allowed_domains = ['weixin.sogou.com']
    start_urls = ['http://weixin.sogou.com/']

    def parse(self, response):
        pass
