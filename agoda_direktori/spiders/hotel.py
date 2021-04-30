import scrapy
import json
import pandas as pd
import csv

class HotelSpider(scrapy.Spider):
    name = 'hotel'
    allowed_domains = ['https://www.agoda.com/graphql/search']
    provinsi = pd.merge(
            pd.read_csv('provinsi.csv'),
            pd.read_csv('provinsi_id.csv').set_index('url'),
            left_on='url',right_index=True, how="left", sort=False
    ).set_index('provinsi_id')

    jsonFile = 'query_agoda.json'
    headers =  {
            'ag-language-locale':'en-us',
            'content-type':'content-type'
        }

    kabko = pd.read_csv('kabko.csv')
    kabko['id_prov'] = kabko.apply(lambda x: int(x.url_prov[-4:]),axis=1)
    kabko.set_index('id_prov')
    kabko = pd.merge(kabko,provinsi,left_on='id_prov',right_index=True, how="left", sort=False)

    def start_requests(self):
        for index,row in self.kabko.iterrows():
            paket = json.load(open(self.jsonFile))
            paket['variables']['CitySearchRequest']['cityId'] = int(row['kabko_id'])
            yield scrapy.http.JsonRequest(
                self.allowed_domains[0],
                headers=self.headers,
                data=paket,
                method="POST",
                callback=self.after_post,
                meta={
                    'details':row,
                    'paket':paket,
                    'data':[]
                },
            )

    def after_post(self, response):
        # print(response.status)
        hotels = json.loads(response.body)
        row = response.meta['details']
        paket = response.meta['paket']
        data = response.meta['data']

        if(len(hotels['data']['citySearch']['properties'])>0):
            paket['variables']['CitySearchRequest']['searchRequest']['page']['pageNumber'] = paket['variables']['CitySearchRequest']['searchRequest']['page']['pageNumber']+1
            self.parse_hotels()
            yield scrapy.http.JsonRequest(
                self.allowed_domains[0],
                headers=self.headers,
                data=paket,
                method="POST",
                callback=self.after_post,
                meta={
                    'details':row,
                    'paket':paket,
                    'data':data.extend(hotels['data']['citySearch']['properties']),
                },
            )

    def parse_hotels(response):
        hotels = json.loads(response.body)
        row = response.meta['details']
        paket = response.meta['paket']
        data = response.meta['data']
        yield {
                "provinsi_id": row.id_prov,
                "provinsi": row.provinsi,
                "provinsi_jumlah": row.total_hotels,
                "kabko_id": row.kabko_id,
                "kabko": row.kabko,
                "kabko_jumlah": row.jumlah_hotel,
                "hotels":data
            }