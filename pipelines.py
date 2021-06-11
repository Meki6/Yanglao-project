# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import csv
class YanglaoPipeline(object):
    def __init__(self):
        self.f = open("yanglao_pipeline.json","wb")#notepad
    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii = False) + ", \n"
        self.f.write(content.encode("utf-8"))
        return item
    def close_spider(self,spider):
        self.f.close()

class YanglaoCsvPipeline(object):
    def __init__(self):
        self.f = open("yanglao.csv", 'wt+', newline='', encoding ='utf-8')
        self.writer = csv.writer(self.f)
    def process_item(self, item, spider):
        textlist = [item['养老机构名称'], item['性质'], item['机构类型'], item['收住对象'],item['床位数'],
                    item['占地面积'], item['月收费'], item['月收费下限'], item['月收费上限'],item['所在地区'],
                    item['地址'], item['邮编'], item['电话']]
        self.writer.writerow(textlist)
        return item

    def close_spider(self, spider):
        self.f.close()