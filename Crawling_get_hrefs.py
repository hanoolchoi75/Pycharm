import requests as rq
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/"

res = rq.get(url)
bs_obj = BeautifulSoup(res.content,'lxml')

lf_items = bs_obj.findAll('div', class_="lf-item")

hrefs = [div.find("a").get('href') for div in lf_items]
print(hrefs)