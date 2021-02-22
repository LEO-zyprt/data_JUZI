# -*- coding: utf-8 -*-
import requests
import pandas as pd

headers = {
    'authority': 'www.itjuzi.com',
    'accept': 'application/json, text/plain, */*',
    'authorization': '"bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE2MTM5NTA1NTAsImV4cCI6MTYxMzk1NDE1MCwibmJmIjoxNjEzOTUwNTUwLCJqdGkiOiIzY0lCZzNhTUZod0pxdjMzIiwic3ViIjo5MjM2NjIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoiRFJST2tkIn0.d_RcU2qe_uA8hgMYN8eBUda2mT0_-jzQEidPrF47WnY"',
    'curlopt_followlocation': 'true',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.itjuzi.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.itjuzi.com/investevent',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '_ga=GA1.2.257741607.1613366932; _gid=GA1.2.2141561476.1613814601; juzi_user=923662; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1613366932,1613814597,1613888587,1613921606; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1613946793; juzi_token=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvdXNlcnNcL3VzZXJfaGVhZGVyX2luZm8iLCJpYXQiOjE2MTM4MTQ2MDUsImV4cCI6MTYxMzk0OTYyOCwibmJmIjoxNjEzOTQ2MDI4LCJqdGkiOiI1eFVUT1VPTGdwTXhCbHFHIiwic3ViIjo5MjM2NjIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoiTGxVaUlTIn0.Np8xBU6IQPz6T3u6jX2PYU-hy4344GHJbfAgpjRHWvk; _gat=1',
}

'''
   请求数据类型
   scope:金融、企业服务、智能硬件、工具软件 
   sub_scope:子行业
   round：轮次
   valuation：
   ipo_platform:
   equity_ratio:
   status:
   prov:省份
   time：2021
   selected：
   location：国内
   hot city：
   currency：
   keyword：
'''

data ='''{"pagetotal":6222,
           "total":0,
           "per_page":20,
           "page":1,"type":1,
           "scope":"金融",
           "sub_scope":[],
           "round":[],
           "valuation":[],
           "valuations":"",
           "ipo_platform":"",
           "equity_ratio":"",
           "status":"",
           "prov":"",
           "city":[],
           "time":[],
           "selected":"",
           "location":"国内",
           "hot_city":"",
           "currency":[],
           "keyword":""}'''

response = requests.post('https://www.itjuzi.com/api/investevents', 
                          headers=headers, 
                          data=data.encode('utf-8'))

'''
需要的数据：
agg_time:
name:
com_scope:
round:
money:
investor[name]:
com_des:
'''
Json_Response = response.json()
#print(Json_Response)

#将json数据格式中的公司信息循环取出
result_json_array = []
for company in Json_Response['data']['data']:
    #investor数据不是非常工整，需要先循环取出投资方
    investor_name_list = []
    for investor in company['investor']:
        investor_name_list.append(investor['name'])
        investor_name_format = '、'.join(investor_name_list) #按照券商老师的要求的格式

    result_jason_row = {'time':company['agg_time'],
                        'name':company['name'],
                        'round':company['round'],
                        'industry':company['com_scope'],
                        'moneny':company['round'],
                        'investor': investor_name_format,
                        'description':company['com_des']}           
    result_json_array.append(result_jason_row)
    
    # 将json格式数据转化为dataframe
df = pd.DataFrame.from_records(result_json_array)
df.to_excel('weekly_report_investment_data.xlsx')

'''需要继续完成的工作
   定义函数可以筛选不同行业
   将日期转化为研究所要求的格式
   对dataframe进行排序
'''