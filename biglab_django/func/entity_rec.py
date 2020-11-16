import jieba
import pandas as pd
import re
import time
import json

from django.http import HttpResponse as response
from django.http import HttpRequest as request

with open('./sourcetxt/person_list.txt',encoding='UTF-8') as f:
    person_list=f.read().splitlines()
with open('./sourcetxt/fund_list.txt',encoding='UTF-8') as f:
    fund_list=f.read().splitlines()
with open('./sourcetxt/company_list.txt',encoding='UTF-8') as f:
    company_list=f.read().splitlines()
with open('./sourcetxt/industry_list.txt',encoding='UTF-8') as f:
    industry_list=f.read().splitlines()
with open('./sourcetxt/stock_list.txt',encoding='UTF-8') as f:
    stock_list=f.read().splitlines()
jieba.set_dictionary('./sourcetxt/entity_dict_labeled.txt')


def entity_rec(request):
    req=request.body
    return req
    print(req)
    entity_d = {'person': [], 'fund': [], 'company': [], 'industry': [], 'stock': []}
    index_l = [0 for i in range(len(news))]
    result = jieba.tokenize(news)
    start = time.time()
    for k in result:
        if k[0] in person_list:
            entity_d['person'] = entity_d['person'] + [k[0]]
            index_l[k[1]:k[2]] = [1 for k in range(k[2] - k[1])]
        if k[0] in fund_list:
            entity_d['fund'] = entity_d['fund'] + [k[0]]
            index_l[k[1]:k[2]] = [2 for k in range(k[2] - k[1])]
        if k[0] in company_list:
            entity_d['company'] = entity_d['company'] + [k[0]]
            index_l[k[1]:k[2]] = [3 for k in range(k[2] - k[1])]
        if k[0] in industry_list:
            entity_d['industry'] = entity_d['industry'] + [k[0]]
            index_l[k[1]:k[2]] = [4 for k in range(k[2] - k[1])]
        if k[0] in stock_list:
            entity_d['stock'] = entity_d['stock'] + [k[0]]
            index_l[k[1]:k[2]] = [5 for k in range(k[2] - k[1])]
    print("--- %s seconds ---" % (time.time() - start))
    print(json.dumps({'entity_d': entity_d, 'index_l': index_l}))
    return json.dumps({'entity_d': entity_d, 'index_l': index_l})