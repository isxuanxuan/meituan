# -*- coding: utf-8 -*-
import scrapy
import json
from meituan.items import MeituanItem
class MeishiSpider(scrapy.Spider):
    name = 'meishi'
    allowed_domains = ['bj.meituan.com']
    baseUrl = 'http://bj.meituan.com/meishi/api/poi/getPoiList?uuid=4ae61de922fe4e48b776.1516937107.2.0.1&platform=1&partner=126&originUrl=http%3A%2F%2Fbj.meituan.com%2Fmeishi%2Fpn1%2F&riskLevel=1&optimusCode=1&cityName=%E5%8C%97%E4%BA%AC&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page={}'
    def start_requests(self):
        for i in range(1,2):
            url = self.baseUrl.format(i)
            yield scrapy.Request(url,callback=self.parse)
    def parse(self, response):
        items = json.loads(response.body)
        for shop in items['data']['poiInfos']:
            poiId = shop['poiId']
            #print(poiId)
            detailPage = 'http://www.meituan.com/meishi/{}/'.format(poiId)
            yield scrapy.Request(detailPage,callback=self.parse_detail)

    #def parse_detail(self,response):

        #sel = json.loads(response.body)
        #for p in sel['data']['infos']:
            #item = MeituanItem()
            #item['name'] = p['name']

            #yield item







