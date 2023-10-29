# Web scraping use cases
# Overview

The main subject of this repository is web scraping. In a nutshell, four web scrapers were developed with Python as use cases to portray different web data extraction scenarios:
1. [HTML tag-based extraction](#1-html-tag-based-extraction)
2. [JSON var-based extraction](#2-json-var-based-extraction)
3. [JSON API-response-based extraction](#3-json-api-response-based-extraction)

## 1. HTML tag-based extraction
### Website: [unesco.org/en](https://whc.unesco.org/en/list/)
To extract the list of world heritage sites designated by UNESCO.

![](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/39f4b500047b3396711f01b34e610b5b4137edbc/output/png/web_scraping_unesco_world_heritage_list.PNG)
<br> py script: [web_scraping_unesco_world_heritage_sites.py](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/4a81a58d6e6c2117170f977c567af27f5529f3b5/src/web_scraping_unesco_world_heritage_sites.py)
<br> csv output: [unesco_world_heritage_sites.csv](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/552f127fab518720510ab781ca205d0ed04ba955/output/csv/unesco_world_heritage_sites.csv)

### Website: [gfmag.com](https://www.gfmag.com/global-data/non-economic-data/best-cities-to-live?page=1)

To extract multiple tables on the world's best cities to live compiled by the Global Finance magazine.

![](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/eab419e273ec771e89dd3fcde2ee76c2aff7be2a/output/png/web_scraping_best_cities_to_live.PNG)
<br> py script: [web_scraping_best_cities_to_live.py](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/b21cee34ba5e76698ab75ebb03ec0c9c3120b280/src/web_scraping_best_cities_to_live.py)
<br>
csv output: [best_cities_to_live.csv](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/0248486b1c2b254345279cbc452aea91655cc6ec/output/csv/best_cities_to_live.csv)

<div align = "right">    
  <a href="#overview">(back to top)</a>
</div>

## 2. JSON var-based extraction
### Website: [www.rollingstone.com](https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/)
To extract the Rolling Stone list on the greatest albums of all time.

![](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/d67dcad63b22f5f485eab4f77f8f71d25c615540/output/png/web_scraping_rs_album_list.PNG)
<br> 
py script: [web_scraping_rs_500_greatest_albums.py](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/df881ee5834538e8acb4010b71c94cd879ea19e2/src/web_scraping_rs_500_greatest_albums.py)
<br>
csv output: [rs_album_list.csv](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/df881ee5834538e8acb4010b71c94cd879ea19e2/output/csv/rs_album_list.csv)

<div align = "right">    
  <a href="#overview">(back to top)</a>
</div>

## 3. JSON API-response-based extraction
### Website: [developer.nytimes.com](https://developer.nytimes.com/docs/books-product/1/overview)
To extract data of all hardcover fiction/nonfiction books for all the best sellers lists of the New York Times.

![](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/4edc51798357c61f1ee51e4b86fc4c512a35d014/output/png/web_scraping_nyt_api_bestsellers_books.PNG)
<br> 
py script: [web_scraping_nyt_api.py](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/f52b3112944609f1b15d3a92b395734c18000e27/src/web_scraping_nyt_api.py)
<br>
csv output: [nyt_bestsellers_books.csv](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/8d04fe6f4afa5465761eee5f4fd81df3d79f7b54/output/csv/nyt_bestsellers_books.csv)

<div align = "right">    
  <a href="#overview">(back to top)</a>
</div>
