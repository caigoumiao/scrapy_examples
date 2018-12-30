# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from weixin_article.items import WeixinArticleItem
from scrapy.http import Response


class ArticlesByPlatSpider(scrapy.Spider):
    name = 'articles_by_plat'
    allowed_domains = ['weixin.sogou.com', 'mp.weixin.qq.com']
    start_urls = ['http://weixin.sogou.com/weixin?']
    plat = '金佳园'

    # 初始处理
    def start_requests(self):
        data = {
            'type': 1,
            'query': self.plat,
            'ie': 'utf8',
            's_from': 'input',
            '_sug_': 'y',
            '_sug_type_': ''
        }
        params = urlencode(data, encoding='utf8')
        url = self.start_urls[0] + params
        yield scrapy.Request(
            url,
            callback=self.parse_1
        )

    def parse_1(self, response):
        print('*' * 100)
        print(response)
        page_url = response.css('#sogou_vr_11002301_box_0 > div > div.txt-box > p.tit > a::attr(href)').extract_first()
        cookies = 'pgv_pvi=7662571520; pt2gguin=o1300361026; RK=f4jF1LUBF+; ptcz=e9301732641ec79174ca7a33ae8af60382f75b54c995919878a5e7636820e1b7; tvfe_boss_uuid=19c7c63ce7d6b53a; pgv_pvid=3942352368; o_cookie=1300361026; eas_sid=u1O5F4E3T7d5S0N3e4p4L5Z156; mobileUV=1_1677ca3859e_94855; pac_uid=1_1300361026; LW_sid=v1J5H435l3I8X9j5C924U3S3K5; LW_uid=t1U52415P388D9x5H9v4s343D6; ua_id=m4Dkj7Tcm61w7sZFAAAAAL7DvLeeldC8mxjuh_ZNO9E=; mm_lang=zh_CN; pgv_info=ssid=s1546278184; sig=h015634ca4c7b73d6c9dea03cfa47f5598230df750c9a023c8c93d18ceb327f29165152a0cafb54563f'
        tmp = {}
        for cookie in cookies.split('; '):
            t = cookie.split('=')
            tmp[t[0]] = t[1]
        print(tmp)
        yield scrapy.Request(
            page_url,
            cookies=tmp
        )

    def parse(self, response):
        print('#' * 100)
        print(response.css('html').extract_first())
        # item=WeixinArticleItem()
        print(response.css('.weui_media_box').extract_first())
        # print(response.css('div.weui_media_box'))
        for media_box in response.css('div.weui_media_box'):
            yield {
                'title': media_box.css('h4.weui_media_title::text').extract_first(),
                'date': media_box.css('p.weui_media_extra_info::text').extarct_first()
            }
        #     item['title']=media_box.css('h4.weui_media_title::text').extract_first()
        #     item['date']=media_box.css('p.weui_media_extra_info::text').extarct_first()
        # yield item
