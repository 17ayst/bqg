# -*- coding: utf-8 -*-
import scrapy
from bqg.items import BqgItem

class TxwsSpider(scrapy.Spider):
    name = 'txws'
    allowed_domains = ['www.yuetutu.com']
    start_urls = ['http://www.yuetutu.com/']

    def parse(self, response):
        lists=response.xpath('//*[@id="hotcontent"]/div[1]/div[1]/dl/dt/a')
        for list in lists:
            url1=list.xpath('@href').extract()[0]
            # print(url1)
            yield response.follow(url1,callback=self.parse1)
            # pass

    def parse1(self, response):
        ml1=response.xpath('//*[@id="list"]/dl/dd/a')
        for ml in ml1:
            url2=ml.xpath('@href').extract()[0]
            # print(url2)
            yield response.follow(url2,callback=self.content)


    def content(self, response):
        item=BqgItem()
        item['name']=response.xpath('//*[@id="wrapper"]/div[3]/div/div[1]/a[3]/text()').extract()
        item['ml']=response.xpath('//*[@id="wrapper"]/div[3]/div/div[2]/h1/text()').extract()
        # item['aimurl']=response.xpath('/html/head/meta[5]/@content').extract()
        a = response.xpath('//*[@id="content"]/text()').extract()
        item['txt']="".join(a)
        yield item