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
# sellers lists of New York Times of the previous 12 months
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
list_dates = date_range(12)

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
    
df_bestsellers.to_csv(f'{path_dir}/nyt_bestsellers.csv', header=True, index=False, encoding='utf-8-sig',sep=';')
df_book_buy_link.to_csv(f'{path_dir}/nyt_buy_link_by_bestseller.csv', header=True, index=False, encoding='utf-8-sig',sep=';')
print("...it has been successfully executed in %0.1fs." % (time() - t_start))