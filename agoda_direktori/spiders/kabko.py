import scrapy
import json
import pandas as pd

class ProvinsiSpider(scrapy.Spider):
    name = 'kabko'
    allowed_domains = ['agoda.com']

    provinsi = pd.merge(
        pd.read_csv('provinsi.csv'),
        pd.read_csv('provinsi_id.csv').set_index('url'),
        left_on='url',right_index=True, how="left", sort=False
    ).apply(lambda x : "https://www.agoda.com/api/cronos/geo/NeighborHoods?pageTypeId=8&objectId="+str(x.provinsi_id),axis=1)

    start_urls = list(provinsi)

    def parse(self, response):
        kabkos = json.loads(response.body)
        for kabko in kabkos:
            yield {
                'url_prov':response.request.url,
                'total_hotels' : kabko['hotels'],
                'url' : kabko['url'],
                'kabko' : kabko['name'],
                'kabko_id' : str(kabko['hotelId']),
            }
