# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_name = scrapy.Field()  # 用户名
    followees = scrapy.Field()  # 用户粉丝
    followers = scrapy.Field()  # 用户关注的人
    introduce = scrapy.Field()  # 简介
    
    head_image = scrapy.Field()  # 头像url
    
    ask = scrapy.Field()  # 提问
    answer = scrapy.Field()  # 回答
   
    collected = scrapy.Field()  # 收藏
   
    main_page = scrapy.Field() #主页url
    _id = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
