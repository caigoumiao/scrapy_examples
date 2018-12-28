# -*- coding: utf-8 -*-
import scrapy


class NetcloudMusicCommentSpider(scrapy.Spider):
    name = 'netcloud_music_comment'
    allowed_domains = ['music.163.com/#/discover/toplist?id=3778678']
    start_urls = ['http://music.163.com/#/discover/toplist?id=3778678/']

    def parse(self, response):
        pass
