import scrapy
import json

class ProvinsiSpider(scrapy.Spider):
    name = 'provinsi'
    allowed_domains = ['agoda.com']
    start_urls = ['https://www.agoda.com/api/id-id/GeoApi/AllStates/4/192/0']

    def parse(self, response):
        provinsis = json.loads(response.body)
        for provinsi in provinsis:
            yield {
                'provinsi':provinsi.get('name'),
                'jumlah_hotel':provinsi.get('hotels'),
                'url':'https://www.agoda.com'+provinsi.get('url'),
            }
