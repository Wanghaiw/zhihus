# -*- coding:utf-8 -*-

from zhihu.settings import *
import scrapy 
from scrapy.http import Request
from zhihu.items import ZhihuItem
import hashlib
import re
import time


class ZhihuSpider(scrapy.Spider):
    name = 'zhspider'

    start_urls = ['https://www.zhihu.com/people/yang-shen-82/answers']

    allowed_domains = ['www.zhihu.com']

    def __init__(self,**kwargs):
        super(ZhihuSpider,self).__init__(**kwargs)
        self.base_url = 'http://www.zhihu.com'
        self.followees_url = 'https://www.zhihu.com/node/ProfileFolloweesListV2'


    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)


    def make_requests_from_url(self,url):
        return Request(url,method='GET',headers=ZHIHU_HEADERS,cookies=ZHIHU_COOKIE)


    def parse(self,response):
        item = ZhihuItem()
        user_name = response.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[1]/h1/span[1]/text()').extract()[0]
        #print response.text
        print user_name
        time.sleep(5)

        if user_name:
            item['user_name'] = user_name
        
        #follow = response.xpath('//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[1]/div')

        #if follow:
        item['followees'] = response.xpath('//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[2]/div/a[1]/div[2]/text()').extract()
        #print item['followees']
        
        
        item['followers'] = response.xpath('//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[2]/div/a[2]/div[2]/text()').extract()
        # print item['followers']
        # time.sleep(5)
        
        item['introduce'] = response.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[1]/h1/span[2]/text()').extract()[0]
        # print item['introduce'] 
        # time.sleep(5)
        
        #item['ellipsis'] = ''.join(response.css('body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div.zm-profile-header.ProfileCard > div.zm-profile-header-main > div > div.top > div.title-section > div::text').extract())

        # item['location'] = ''.join(response.css('.location .topic-link::text').extract())

        # item['major'] = ''.join(response.css('.business .topic-link::text').extract())

        head_url = response.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[1]/img/@src').extract()[0]
        #print head_url
        #time.sleep(5)
        arr = []
        arr.append(head_url)
        item['head_image'] = head_url
        item['image_urls'] = arr

        item['ask'] = (response.xpath('//*[@id="ProfileMain"]/div[1]/ul/li[4]/a/span/text()').extract())[0]
        #print item['ask']
       
        
        item['answer'] = response.xpath('//*[@id="ProfileMain"]/div[1]/ul/li[2]/a/span/text()').extract()[0]
        # print item['answer']
        # time.sleep(5)
        
        #item['articles'] = int(''.join(response.css('.item:nth-child(4) .num::text').extract()))

        item['collected'] = response.xpath('//*[@id="ProfileMain"]/div[1]/ul/li[5]/a/span/text()').extract()[0]

       


        #item['public_editor'] = re.findall(r'\d+',response.xpath('//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[1]/div[2]/div[5]/div/a/text()').extract()[0])
        
        #item['views'] = int(''.join(response.css('.zg-gray-normal strong::text').extract()))

        if response.url:
            item['main_page'] = response.url
        print response.url
        
        item['_id'] = hashlib.sha1(response.url).hexdigest()
        yield item

        urls = response.xpath('//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[2]/div/a[1]/@href').extract()
     

        time.sleep(5)
        if urls:
            for url in urls:
                url = 'https://www.zhihu.com' + url
                print url
                yield scrapy.Request(url=url, callback=self.parse_followers,headers=ZHIHU_HEADERS, cookies=ZHIHU_COOKIE)


    def parse_followers(self, response):
        urls = response.xpath('//*[@id="Profile-following"]/div[2]/div/div/div[1]/h2/div/span/div/div/a/@href').extract()
        
        if urls:
            for url in urls:
                url = self.base_url + url

                print url
                time.sleep(5)
                yield scrapy.Request(url=url, callback=self.parse,headers=ZHIHU_HEADERS, cookies=ZHIHU_COOKIE)