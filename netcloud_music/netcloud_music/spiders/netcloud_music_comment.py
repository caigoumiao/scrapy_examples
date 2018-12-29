# -*- coding: utf-8 -*-
import scrapy


class NetcloudMusicCommentSpider(scrapy.Spider):
    name = 'netcloud_music_comment'
    allowed_domains = ['music.163.com/#']
    start_urls = ['https://music.163.com/#/song?id=1334647784']
    index = 1

    def parse(self, response):
        print(response)
        # comment-box > div > div.m-cmmt > div.cmmts.j-flag > div:nth-child(3)
        # comment-box > div > div.m-cmmt > div.cmmts.j-flag > div:nth-child(3) > div.cntwrap > div:nth-child(1) > div
        # // *[ @ id = "comment-box"] / div / div[2] / div[2] / div[2] / div[2] / div[1] / div / text()
        # print(response.css('#comment-box > div > div.m-cmmt > div.cmmts.j-flag > div:nth-child(3) > div.cntwrap > div:nth-child(1) > div::text').extract())
        # print(response.css('#g_nav2 > div > ul > li:nth-child(2) > a::attr(href)').extract_first())
        # print(response.xpath('// *[ @ id = "comment-box"] / div / div[2] / div[2] / div[2] / div[2] / div[1] / div / text()').extract_first())
        # for song in response.css('div.tt'):
        #     song_page = song.css('a::attr(href)').extract_first()
        #     print('%d--%s'%(self.index, song_page))
        #     self.index += 1
