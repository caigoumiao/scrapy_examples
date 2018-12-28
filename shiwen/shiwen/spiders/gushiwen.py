# -*- coding: utf-8 -*-
import scrapy


class GushiwenSpider(scrapy.Spider):
    name = 'gushiwen'
    allowed_domains = ['www.gushiwen.org']
    start_urls = ['https://www.gushiwen.org/shiwen/default_0AA1.aspx']
    id = 1

    def parse(self, response):
        print('###'*20)
        for shi in response.css('div.left > div.sons'):
            selector = shi.css('div.cont > div.contson > p')
            if len(selector) != 0:
                s = shi.css('div.cont > div.contson > p::text').extract()
            else:
                s = shi.css('div.cont > div.contson::text').extract()
            content = '\n'.join(s)
            yield {
                'id': self.id,
                'title': shi.css('div.cont > p:nth-child(2) > a > b::text').extract_first(),
                'dynasty': shi.css('div.cont > p.source > a:nth-child(1)::text').extract_first(),
                'author': shi.css('div.cont > p.source > a:nth-child(3)::text').extract_first(),
                'content': content
            }
            self.id += 1

        next_page = response.css('#FromPage > div > a.amore::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
