"""
Web Scraping: The Greatest Books of All Time
Created on Sun Oct 22 11:25:21 2023
@author: IvoBarros
"""
import requests
from bs4 import BeautifulSoup 
import pandas as pd 
import os
from time import time, sleep
from random import randint

def get_website_pages(nr_pages):
    """
    To compile a list of pages from the Greatest Books website 
    
    Args:
        nr_pages : int
        
    Returns:
        list
    """
    website = 'https://thegreatestbooks.org/'
    links_pages = []
    
    for i in range(2,nr_pages+1):  
        links_pages.append(f'{website}?page={str(i)}')
    
    links_pages.append(website)
        
    return links_pages

def extract_books_attributes(links):
    """
    To extract and store the attributes of every single book of the list
 
    Args:
        links : list
        
    Returns:
        DataFrame
    """
    web_data = {"position": [], "title": [], "author": []}
    
    for i in links:
        try:
            page = requests.get(i)
            soup = BeautifulSoup(page.content, 'html.parser') 
            
            for j in soup.find_all('div',attrs={'class':'list-body'}):
                for k in j.find_all("h4"):
                    web_data['position'].append(k.text.split()[0])    
                    for l in k.find_all("a"):
                        if 'authors' in l['href']:     
                            web_data['author'].append(l.text)
                        elif 'items' in l['href']:
                            web_data['title'].append(l.text)
        except:
            pass   
        sleep(randint(2,5))

    return  pd.DataFrame(web_data)

print("The script is running...")
t_start = time()

#==============================================================================
# 1. WEB SCRAPING
#==============================================================================
path_parent_dir = os.path.dirname(os.getcwd())
path_output_csv = f'{path_parent_dir}\output\csv'
links = get_website_pages(6)
df_the_greatest_books = extract_books_attributes(links)

#==============================================================================
# 2. DATA TRANSFORMATION
#==============================================================================
df_the_greatest_books['position'] = df_the_greatest_books['position'].astype(int)
df_the_greatest_books = df_the_greatest_books.sort_values(by=['position'], ascending=True).reset_index(drop=True)
df_the_greatest_books.to_csv(f'{path_output_csv}/the_greatest_books_of_all_time.csv', header=True, index=False, encoding='utf-8-sig',sep=';')
print("...it has been successfully executed in %0.1fs." % (time() - t_start))