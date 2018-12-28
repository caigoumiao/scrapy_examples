# -*- coding: utf-8 -*-
import scrapy


class NetcloudMusicCommentSpider(scrapy.Spider):
    name = 'netcloud_music_comment'
    allowed_domains = ['music.163.com/#/discover/toplist?id=3778678']
    start_urls = ['http://music.163.com/#/discover/toplist?id=3778678/']
    index = 1

    def parse(self, response):
        print(response.css('div.ttt'))
        for song in response.css('div.ttt'):
            song_page = song.css('a::attr(href)').extract_first()
            print(self.index + '------' + song_page)
            self.index += 1
