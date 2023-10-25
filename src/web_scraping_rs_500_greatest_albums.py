"""
Web Scraping: The 500 Greatest Albums of All Time - Rolling Stone website
Created on Mon Nov 28 11:02:43 2021
@author: IvoBarros
"""
import requests
import json
import re
import pandas as pd
from time import time, sleep
from random import randint
import os
import os.path
import lxml.html

def strip_html(string):
    """
    To remove html entities from text
    Approach proposed on Stack Overflow (question 753052, PascalVKooten)
 
    Args:
        string : str
        
    Returns:
        str
    """   
    return lxml.html.fromstring(string).text_content() if string else ''

def extract_album_attributes(links):
    """
    To extract and store the attributes of every single album from the Rolling Stone list
 
    Args:
        links : list
        
    Returns:
        DataFrame
    """  
    web_data = {'position': [], 'title': [], 'subtitle': [], 'description': []}
    
    for i in pages:
        url = f'https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/{str(i)}'
        page = requests.get(url, allow_redirects=False).text
        var_gallery = json.loads(re.search(r"var pmcGalleryExports = (\{.*\})", page).group(1))['gallery']
    
        for j in var_gallery:
            web_data['position'].append(j['positionDisplay'])    
            web_data['title'].append(strip_html(j['title']))
            web_data['subtitle'].append(strip_html(j['subtitle']))
            web_data['description'].append(strip_html(j['description']))
            
        sleep(randint(2,5))
        
    return pd.DataFrame(web_data)

print("The script is running...")
t_start = time()

#==============================================================================
# 1. WEB SCRAPING
#==============================================================================
path_parent_dir = os.path.dirname(os.getcwd())
path_output_csv = f'{path_parent_dir}\output\csv'
pages = ["arcade-fire-%ef%bb%bffuneral-1062733","linda-mccartney-and-paul-ram-1062783",\
         "the-go-gos-beauty-and-the-beat-1062833","stevie-wonder-music-of-my-mind-2-1062883",\
         "shania-twain-come-on-over-1062933","buzzcocks-singles-going-steady-2-1062983",\
         "sade-diamond-life-1063033","bruce-springsteen-nebraska-3-1063083",\
         "the-band-music-from-big-pink-2-1063133","jay-z-the-blueprint-3-1063183"]
df_rs_album_list = extract_album_attributes(pages)

#==============================================================================
# 2. TEXT DATA CLEANING
#==============================================================================
df_rs_album_list['title'] = df_rs_album_list['title'].str.replace(", ’", ", ‘")
title_split = df_rs_album_list['title'].str.split(', ‘', n=1, expand=True)
df_rs_album_list['album'] = title_split[1].str[:-1]
df_rs_album_list['artist'] = title_split[0]
subtitle_split = df_rs_album_list['subtitle'].str.split(', ', n=1, expand=True)
df_rs_album_list['record_label' ]= subtitle_split[0]
df_rs_album_list['year'] = subtitle_split[1]
df_rs_album_list.drop(columns=['title', 'subtitle'], inplace = True)
df_rs_album_list = df_rs_album_list[[i for i in df_rs_album_list.columns if i!=df_rs_album_list.columns[1]] + [df_rs_album_list.columns[1]]]
df_rs_album_list.to_csv(f'{path_output_csv}/rs_album_list.csv', header=True, index=False, encoding='utf-8-sig',sep=';')
print("...it has been successfully executed in %0.1fs." % (time() - t_start))

# df1['count_apost'] = df1['title'].str.count('|'.join(['‘','’','”']))
# df1['count_comma'] = df1['title'].str.count(',')
# df1['test'] = df1.apply(lambda x: 1 if x.album == x.album_2 else 0, axis=1)