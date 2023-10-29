"""
Web Scraping: World's Best Places To Live - Global Finance website
Created on Sat Oct 28 22:27:03 2023
@author: IvoBarros
"""
import requests
from bs4 import BeautifulSoup 
import pandas as pd 
import os
from time import time, sleep
from random import randint

print("The script is running...")
t_start = time()

#==============================================================================
# WEB SCRAPING
#==============================================================================
path_parent_dir = os.path.dirname(os.getcwd())
path_output_csv = f'{path_parent_dir}\output\csv'
website = 'https://www.gfmag.com/global-data/non-economic-data/best-cities-to-live'
links_pages = [f'{website}?page={str(i)}' for i in range(1,3)]
list_dfs_temp = list()

for i in links_pages:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    year = ''.join([j.text[-4:] for j in soup.select(".align-right:has(.highlighted)")])   
        
    for k in soup.find_all('table',attrs={'class':'bankrate_table'}):
        table_temp = pd.read_html(str(k))
        table_temp = table_temp[0]
        table_temp.insert(0, "Year", year)
        list_dfs_temp.append(table_temp)
    
    sleep(randint(5,6))

df_best_cities = pd.concat(list_dfs_temp, axis=0)
df_best_cities.to_csv(f'{path_output_csv}/best_cities_to_live.csv', header=True, index=False, encoding='utf-8-sig',sep=';')
print("...it has been successfully executed in %0.1fs." % (time() - t_start))