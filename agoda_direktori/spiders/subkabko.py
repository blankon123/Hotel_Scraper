import scrapy
import json
import pandas as pd

class SubkabkoSpider(scrapy.Spider):
    name = 'subkabko'
    allowed_domains = ['agoda.com']
    kabko = pd.read_csv('kabko.csv').apply(lambda x : "https://www.agoda.com/api/cronos/geo/NeighborHoods?pageTypeId=5&objectId="+str(x.kabko_id),axis=1)

    start_urls = list(kabko)

    def parse(self, response):
        kabkos = json.loads(response.body)
        for kabko in kabkos:
            yield {
                'url_kabko':response.request.url,
                'total_hotels' : kabko['hotels'],
                'url' : kabko['url'],
                'subkabko' : kabko['name'],
                'subkabko_id' : str(kabko['hotelId']),
            }
