# -*- coding: utf-8 -*-
# from typing import Any

from scrapy.selector import Selector
import scrapy
import re



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

class YanglaobotSpider(scrapy.Spider):
    pagenum = 1
    name = 'yanglaobot'
    allowed_domains = ['www.yanglaocn.com/yanglaoyuan/yly/?RgSelect=1']
    start_urls = ['http://www.yanglaocn.com/yanglaoyuan/yly/?RgSelect=02101&page=1']#上海的第一页


    def parse(self, response):
        num = 1000
        for nursinghome in response.xpath('//*[@id="yly_list_div"]/div'):#//*[@id="yly_list_div"]/div[2]/div/a/div[2]/ul[1]/li/span
            num += -1
            item = YanglaoItem()
            if nursinghome.xpath('div/a/div[2]/ul[1]/li/span/text()').get() is not None:#去除广告
                item['养老机构名称'] = nursinghome.xpath('div/a/div[2]/ul[1]/li/span/text()').get()
                detail_link = nursinghome.xpath('div/a/@href').get()
                yield scrapy.Request(detail_link, meta={'item':item}, priority = num, callback = self.parse_detail, dont_filter = True)#点进页面去爬详细信息

        ##############下一页操作#################
        if self.pagenum < 92:
            self.pagenum += 1
            url = 'http://www.yanglaocn.com/yanglaoyuan/yly/?RgSelect=02101&page=%d' % self.pagenum
            yield scrapy.Request(url, callback=self.parse, dont_filter = True)
    def parse_detail(self, response):
        scs = Selector(response)
        item = response.meta['item']
        #
        data = scs.xpath('//*[@id="BasicInformation"]').get()
        item['占地面积']=re.findall('<span>占地面积：</span>(.*?)</div>',data)[0]
        item['床位数'] = re.findall('<span>床位数量：</span>(.*?)</div>', data)[0]
        item['性质'] = re.findall('<span>机构性质：</span>(.*?)</div>', data)[0]
        item['机构类型'] = re.findall('<span>机构类型：</span>(.*?)</div>', data)[0]
        item['收住对象'] = "".join(re.findall('<span>收住对象：</span>(.*?)</div>', data)[0]).replace("\xa0"," ")
        item['月收费'] = re.findall('<span>收费区间：</span>(.*?)</div>', data)[0]
        item['月收费下限'] = re.findall('<span>收费区间：</span>(.*?)-', data)[0]
        item['月收费上限'] = re.findall('<span>收费区间：</span>[0-9]*-(.*?)</div>', data)[0]

        data = response.xpath('//*[@id="ContactUs"]').get()
        item['所在地区'] = re.findall('<span>所在地区：</span>(.*?)</div>', data)[0]
        item['地址'] = re.findall('<span>联系地址：</span>(.*?)</div>', data)[0]
        item['邮编'] = re.findall('<span>邮政编码：</span>(.*?)</div>', data)[0]
        item['电话'] = "".join(re.findall('<span>固定电话：</span>((.|\n)*?)</div>', data)[0]).strip('\n\t\t\t') #但是是动态加载的。。还需要其他操作才能让爬虫读到
        yield item




