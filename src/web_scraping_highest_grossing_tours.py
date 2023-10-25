"""
Web Scraping: The highest grossing concert tours of all time - Wikipedia website
Created on Sun Oct 22 17:45:57 2023
@author: IvoBarros
"""
import requests
from bs4 import BeautifulSoup 
import pandas as pd 
import os
from time import time

print("The script is running...")
t_start = time()

#==============================================================================
# WEB SCRAPING
#==============================================================================
path_parent_dir = os.path.dirname(os.getcwd())
path_output_csv = f'{path_parent_dir}\output\csv'
website = 'https://en.wikipedia.org/wiki/List_of_highest-grossing_concert_tours'
page = requests.get(website)
soup = BeautifulSoup(page.content, 'html.parser') 

dict_tables = {} 
for i in soup.find_all('table',attrs={'class':'wikitable sortable plainrowheaders'}):
    table_temp = pd.read_html(str(i))
    dict_tables.update({i.caption.text.strip(): table_temp[0]})

for k, v in dict_tables.items():
    v.drop(columns=['Ref.'], inplace = True)
    v.to_csv(f'{path_output_csv}/{k.replace(" ","_").replace("-","_").lower()}.csv', header=True, index=False, encoding='utf-8-sig',sep=';')

print("...it has been successfully executed in %0.1fs." % (time() - t_start))