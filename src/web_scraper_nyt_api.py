"""
NYT BOOKS API
Created on Sun Jan  8 20:17:27 2023
@author: IvoBarros
"""
import pandas as pd
import requests
import json
import time 
import datetime
from datetime import date

"""
full-overview:
Get all books for all the Best Sellers lists for specified date
"""
def nyt_api_response(date):
    nyt_api_key = '9jjx32KvON11MS6WzaXW4l6zWuoWODXC'
    url = "https://api.nytimes.com/svc/books/v3/lists/full-overview.json?"
    requestHeaders = {"Accept": "application/json"}
    response = requests.get(url + 'published_date=' + date + '&api-key=' + nyt_api_key, headers=requestHeaders)
    text = response.text
    time.sleep(6)
    return text 

def parse_response(response, api_list_id, list_dfs_temp):   
    try:
        json_data = json.loads(response)
        list_published_date = json_data['results']['published_date']
        for j in api_list_id:
            json_fict_nonfict = [k for k in json_data['results']['lists'] if k['list_id'] == j]
            df_temp = pd.json_normalize(json_fict_nonfict[0]['books'])
            df_temp.insert(0, "published_date", list_published_date)
            df_temp.insert(1, "list_id", str(j))
            list_dfs_temp.append(df_temp)
    except:
        pass
    return list_dfs_temp


list_dates = ['2021-01-22','2023-01-22']

# list_dates = [datetime.date(y, m, d) for y in range(date.today().year - 3, date.today().year + 1) 
#                                      for m in range(1,13) 
#                                      for d in [1,7,14,21,28] 
#                                      if datetime.date(y, m, d) < date.today()]

#HARDCOVER FICTION AND HARDCOVER NONFICTION
master_list_dfs = list()

for i in list_dates:
    list_dfs_temp = list()
    master_list_dfs.extend(parse_response(nyt_api_response(str(i)), [1,2], list_dfs_temp))

df_bestsellers = pd.concat(master_list_dfs, axis=0)


 


# list_dates = ['2021-01-22','2023-01-22']
    



api_published_date = '2021-01-22'
nyt_api_key = '9jjx32KvON11MS6WzaXW4l6zWuoWODXC'
requestHeaders = {"Accept": "application/json"}
url = "https://api.nytimes.com/svc/books/v3/lists/full-overview.json?"
response = requests.get(url + 'published_date=' + api_published_date + '&api-key=' + nyt_api_key, headers=requestHeaders)
text = response.text
# print(json.dumps(text, indent=4))
json_data = json.loads(text)


t_01 = json_data['results']
t_02 = json_data['results']['lists'][2]
t_02_02 = json_data['results']['lists'][3]

t_03 = json_data['results']['lists'][2]['books']
t_04 = json_data['results']['lists'][2]['books'][0]['buy_links']


for i in range(0,5):
    print(json_data['results']['lists'][2]['books'][i]['buy_links'])

test_03=pd.json_normalize(t_03)


# z=a['results']['lists']['list_id']['books']['title']


test=pd.json_normalize(t_01)

df_temp = pd.DataFrame()
for i in t_01: 
    for k in t_01['lists']:
        if k['list_id'] == 2:
            for i in k['books']:
                df_temp = pd.concat([df_temp, pd.json_normalize(i)])
                print(i['title'])
            


json_fict_nonfict = [j for j in json_data['results']['lists'] if j['list_id'] in (1,2)]
# df_test = pd.json_normalize(test)
            
        #     print(k)
        
        # if t['lists']=='2':
        #     print(t['lists'])
            
        #     for j in k['books']:
        #         print(j)
                
        #         df_temp = pd.concat([df_temp, pd.json_normalize(j)])



############################################################################################

# api_published_date = '2021-01-22'
# nyt_api_key = '9jjx32KvON11MS6WzaXW4l6zWuoWODXC'
# requestHeaders = {"Accept": "application/json"}
# url = "https://api.nytimes.com/svc/books/v3/lists/full-overview.json?"
# response = requests.get(url + 'published_date=' + api_published_date + '&api-key=' + nyt_api_key, headers=requestHeaders)
# text = response.text
# # print(json.dumps(text, indent=4))
# json_data = json.loads(text)

# list_dates = []
# for i in range(0,4):
#     for j in range(1,13):
#         for k in range(1,32,7):          
#             print('202'+str(i) + '-' + str(j).zfill(2) + '-'+ str(k).zfill(2))        
#             date_prep = '202'+str(i) + '-' + str(j).zfill(2) + '-'+ str(k).zfill(2)
#             list_dates.append(date_prep)

# for j in range(1,13):
#     print(str(j).zfill(2))

# for i in range(0,4):
#     print('202'+str(i))
    
# for i in range(1,32,5):
#     print(str(i).zfill(2))