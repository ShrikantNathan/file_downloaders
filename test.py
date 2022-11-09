import os
from typing import Dict
import requests
import pprint
import shutil
import wget

test_url = requests.get('https://dummyjson.com/products')
resp_test_url = test_url.json()
prod_url = resp_test_url.get('products')
all_prod_imag_url, all_webp_ext = list(), list()
# print(pprint.pprint(prod_url))
for i in range(len(prod_url)):
    for prod_key, prod_val in prod_url[i].items():
        if prod_key == "images":
            all_prod_imag_url.append(prod_val)

for i in range(len(all_prod_imag_url)):
    print(f'------------------------Element {i}----------------------------')
    for j in range(len(all_prod_imag_url[i])):
        if str(all_prod_imag_url[i][j]).endswith('.webp'):
            all_webp_ext.append(all_prod_imag_url[i][j])
            all_prod_imag_url[i].remove(all_prod_imag_url[i][j])
        else:
            wget.download(all_prod_imag_url[i][j])
        print(all_prod_imag_url[i][j])
    print(f'------------------------Element {i} end------------------------')

print('all webp extensions:', all_webp_ext)