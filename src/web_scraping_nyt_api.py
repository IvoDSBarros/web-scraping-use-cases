"""
Web Scraping: New York Times Books API
Created on Sun Jan  8 20:17:27 2023
@author: IvoBarros
"""
import pandas as pd
import requests
import json
from time import time, sleep
import datetime
from random import randint
from dateutil.relativedelta import relativedelta
import os
import os.path

#==============================================================================
# To extract data of all hardcover fiction/nonfiction books for all the best 
# sellers lists of the New York Times of the previous 24 months
#==============================================================================

def nyt_api_response(date):
    """
    To send a request to the New York Times Book API and get a response

    Args:
        date : str
        
    Returns:
        str
    """
    nyt_api_key = '9jjx32KvON11MS6WzaXW4l6zWuoWODXC'
    url = "https://api.nytimes.com/svc/books/v3/lists/full-overview.json?"
    requestHeaders = {"Accept": "application/json"}
    response = requests.get(url + 'published_date=' + date + '&api-key=' + nyt_api_key, headers=requestHeaders)
    text = response.text
    sleep(randint(5,6))
    return text 

def parse_data(response, api_list_id, list_dfs_temp):
    """
    To parse json response from the API
 
    Args:
        response : str
        api_list_id : list
        list_dfs_temp : list
        
    Returns:
        DataFrame
    """    
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

def date_range(nr_months):
    """
    To generate a list of dates between the current date and a given past date
    for a maximum of 24 previous months
 
    Args:
        nr_months : int
        
    Returns:
        list
    """
    start_date = datetime.date.today() - relativedelta(months=nr_months)
    end_date = datetime.date.today()
    
    if nr_months >=0 and nr_months <=24:
        list_dates = pd.date_range(start=start_date, end=end_date, freq='W').date.tolist()
    
    return list_dates                                     
           
print("The script is running...")
t_start = time()

#==============================================================================
# 1. WEB SCRAPING
#==============================================================================
path_dir = os.getcwd()
master_list_dfs = list()
list_dates = date_range(24)

for i in list_dates:
    list_dfs_temp = list()
    master_list_dfs.extend(parse_data(nyt_api_response(str(i)), [1,2], list_dfs_temp))

df_bestsellers = pd.concat(master_list_dfs, axis=0)

#==============================================================================
# 2. DATA TRANSFORMATION
#==============================================================================
df_book_buy_link = df_bestsellers[['book_uri', 'buy_links']].groupby(by='book_uri').first().reset_index()
dict_buy_links = {'amazon': 0, 'apple_books': 1, 'barnes_and_noble': 2, 'books_a_million': 3, 'bookshop': 4, 'indie_bound': 5}

for k, v in dict_buy_links.items():
    df_book_buy_link[f'buy_links_{k}'] = df_book_buy_link['buy_links'].apply(lambda i: i[v]['url'])

df_book_buy_link.drop(columns=['buy_links'], inplace = True)
df_bestsellers.drop(columns=['buy_links'], inplace = True)
    
df_bestsellers.to_csv(f'{path_dir}/output/nyt_bestsellers_books.csv', header=True, index=False, encoding='utf-8-sig',sep=';')
df_book_buy_link.to_csv(f'{path_dir}/output/nyt_buy_link_by_bestseller_book.csv', header=True, index=False, encoding='utf-8-sig',sep=';')
print("...it has been successfully executed in %0.1fs." % (time() - t_start))

# full-overview:
# Get all books for all the Best Sellers lists for specified date
# HARDCOVER FICTION AND HARDCOVER NONFICTION


# api_published_date = '2021-01-22'
# nyt_api_key = '9jjx32KvON11MS6WzaXW4l6zWuoWODXC'
# requestHeaders = {"Accept": "application/json"}
# url = "https://api.nytimes.com/svc/books/v3/lists/full-overview.json?"
# response = requests.get(url + 'published_date=' + api_published_date + '&api-key=' + nyt_api_key, headers=requestHeaders)
# text = response.text
# # print(json.dumps(text, indent=4))
# json_data = json.loads(text)


# t_01 = json_data['results']
# t_02 = json_data['results']['lists'][2]
# t_02_02 = json_data['results']['lists'][3]

# t_03 = json_data['results']['lists'][2]['books']
# t_04 = json_data['results']['lists'][2]['books'][0]['buy_links']
# t_05 = json_data['results']['lists'][2]['books'][0]['buy_links'][0]['url']


# for i in range(0,5):
#     test = json_data['results']['lists'][2]['books'][i]['buy_links']
#     for j in test:
#         print(j['name'] + ": " +  j['url'])


# test_03=pd.json_normalize(t_03)


# # z=a['results']['lists']['list_id']['books']['title']


# test=pd.json_normalize(t_01)

# df_temp = pd.DataFrame()
# for i in t_01: 
#     for k in t_01['lists']:
#         if k['list_id'] == 2:
#             for i in k['books']:
#                 df_temp = pd.concat([df_temp, pd.json_normalize(i)])
#                 print(i['title'])
            


# json_fict_nonfict = [j for j in json_data['results']['lists'] if j['list_id'] in (1,2)]
# # df_test = pd.json_normalize(test)
            
#         #     print(k)
        
#         # if t['lists']=='2':
#         #     print(t['lists'])
            
#         #     for j in k['books']:
#         #         print(j)
                
#         #         df_temp = pd.concat([df_temp, pd.json_normalize(j)])



# ############################################################################################

# # api_published_date = '2021-01-22'
# # nyt_api_key = '9jjx32KvON11MS6WzaXW4l6zWuoWODXC'
# # requestHeaders = {"Accept": "application/json"}
# # url = "https://api.nytimes.com/svc/books/v3/lists/full-overview.json?"
# # response = requests.get(url + 'published_date=' + api_published_date + '&api-key=' + nyt_api_key, headers=requestHeaders)
# # text = response.text
# # # print(json.dumps(text, indent=4))
# # json_data = json.loads(text)

# # list_dates = []
# # for i in range(0,4):
# #     for j in range(1,13):
# #         for k in range(1,32,7):          
# #             print('202'+str(i) + '-' + str(j).zfill(2) + '-'+ str(k).zfill(2))        
# #             date_prep = '202'+str(i) + '-' + str(j).zfill(2) + '-'+ str(k).zfill(2)
# #             list_dates.append(date_prep)

# # for j in range(1,13):
# #     print(str(j).zfill(2))

# # for i in range(0,4):
# #     print('202'+str(i))
    
# # for i in range(1,32,5):
# #     print(str(i).zfill(2))






