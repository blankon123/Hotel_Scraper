import pandas as pd
import json
# provinsi = pd.read_csv('provinsi.csv')
# provinsi.jumlah_hotel = pd.to_numeric(provinsi.jumlah_hotel)
# print(provinsi.sum(axis=0))

# provinsi = pd.merge(
#                 pd.read_csv('provinsi.csv'),
#                 pd.read_csv('provinsi_id.csv').set_index('url'),
#                 left_on='url',right_index=True, how="left", sort=False
#             ).apply(lambda x : "ctId="+str(x.provinsi_id),axis=1)
# print(provinsi)

# provinsi = pd.merge(
#         pd.read_csv('provinsi.csv'),
#         pd.read_csv('provinsi_id.csv').set_index('url'),
#         left_on='url',right_index=True, how="left", sort=False
# ).set_index('provinsi_id')

# kabko = pd.read_csv('kabko.csv')
# kabko['id_prov'] = kabko.apply(lambda x: int(x.url_prov[-4:]),axis=1)
# kabko.set_index('id_prov')
# kabko = pd.merge(kabko,provinsi,left_on='id_prov',right_index=True, how="left", sort=False)

# print(kabko.columns)
# import json
a = json.load(open('result_dumy.json'))
b = []
c = a['data']['citySearch']['properties']
for i in range(0,10):
        b.extend(c)
print(len(a)>0)
print(len(b))
print(len(c))

# import json
# import pandas as pd

# provinsi = pd.merge(
#         pd.read_csv('provinsi.csv'),
#         pd.read_csv('provinsi_id.csv').set_index('url'),
#         left_on='url',right_index=True, how="left", sort=False
# ).set_index('provinsi_id')
# jsonFile = 'query_agoda.json'
# kabko = pd.read_csv('kabko.csv')
# kabko['id_prov'] = kabko.apply(lambda x: int(x.url_prov[-4:]),axis=1)
# kabko.set_index('id_prov')
# kabko = pd.merge(kabko,provinsi,left_on='id_prov',right_index=True, how="left", sort=False)

# for index,row in kabko.iterrows():
#         paket = json.load(open(jsonFile))
#         paket['CitySearchRequest']['cityId'] = int(row['kabko_id'])
        # print(paket['CitySearchRequest']['cityId'])

# paket = open('query_graphql.txt', 'r').read().replace('17193',str(99))
# print(paket)