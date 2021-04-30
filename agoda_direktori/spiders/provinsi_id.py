import scrapy
import json
import pandas as pd

class ProvinsiSpider(scrapy.Spider):
    name = 'provinsi_id'
    allowed_domains = ['agoda.com']
    start_urls = list(pd.read_csv('provinsi.csv').url)

    def parse(self, response):
        html = response.body
        tag_begin = str(html).find('objectId: ')
        provinsi_id = str(html)[tag_begin+10:tag_begin+14]
        yield {
            'url':response.request.url,
            'provinsi_id':provinsi_id,
        }
