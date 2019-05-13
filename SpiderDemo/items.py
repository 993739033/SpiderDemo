# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderdemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MKItem(scrapy.Item):
    #标题
    title = scrapy.Field()
    #课程Url
    m_url = scrapy.Field()
    #图片Url
    image_url = scrapy.Field()
    #大图url
    image_big_url = scrapy.Field()