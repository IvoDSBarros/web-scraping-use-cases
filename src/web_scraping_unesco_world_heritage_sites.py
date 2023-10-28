"""
Web Scraping: World Heritage List by UNESCO
Created on Sat Oct 28 19:13:55 2023
@author: IvoBarros
"""
import requests
from bs4 import BeautifulSoup 
import pandas as pd
import re
import os
from time import time

print("The script is running...")
t_start = time()

#==============================================================================
# WEB SCRAPING
#==============================================================================
path_parent_dir = os.path.dirname(os.getcwd())
path_output_csv = f'{path_parent_dir}\output\csv'
website = 'https://whc.unesco.org/en/list/'
page = requests.get(website)
soup = BeautifulSoup(page.content, 'html.parser') 

web_data = {'country': [],'property_name': [],'property_category': [],'country_link': [],'property_link': []}          

for i in soup.find_all('div',attrs={'class':'card bg-none border mt-4'}):
    for j, k in zip(i.find_all('a',attrs={'class':'text-dark'}),i.find_all('div',attrs={'class':'list_site'})):
        for l in k.find_all('li'):
            for m in l.find_all('a'):
                if m['href'].startswith('/en/list/') and m.has_attr('style')==False:
                    web_data['country'].append(j.text)
                    web_data['property_name'].append(m.text)
                    web_data['country_link'].append(f"https://whc.unesco.org{j['href']}")
                    web_data['property_link'].append(f"https://whc.unesco.org{m['href']}")            
                    property_status_raw = ''.join(re.findall('li class=".*?"', str(l)))
                    web_data['property_category'].append(property_status_raw.split('"')[1])
                            
df_unesco_list = pd.DataFrame(web_data)
df_unesco_list.to_csv(f'{path_output_csv}/unesco_world_heritage_list.csv', header=True, index=False, encoding='utf-8-sig',sep=';')
print("...it has been successfully executed in %0.1fs." % (time() - t_start))