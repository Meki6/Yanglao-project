# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YanglaoItem(scrapy.Item):
    # define the fields for your item here like:
    养老机构名称 = scrapy.Field()
    性质 = scrapy.Field()
    机构类型 = scrapy.Field()
    收住对象 = scrapy.Field()
    床位数 = scrapy.Field()
    占地面积 = scrapy.Field()
    月收费 = scrapy.Field()
    月收费下限 = scrapy.Field()
    月收费上限 = scrapy.Field()
    所在地区 = scrapy.Field()
    地址 = scrapy.Field()
    邮编 = scrapy.Field()
    电话 = scrapy.Field()
    # pass
