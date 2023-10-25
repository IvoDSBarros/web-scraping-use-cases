# Web scraping use cases
# Overview

The main subject of this repository is web scraping. In a nutshell, four web scrapers were developed with Python as use cases to portray different web data extraction scenarios:
1. [HTML tag-based extraction](#1-html-tag-based-extraction)
2. [JSON var-based extraction](#2-json-var-based-extraction)
3. [JSON API-response-based extraction](#3-json-api-response-based-extraction)

## 1. HTML tag-based extraction
### Website: [thegreatestbooks.org](https://thegreatestbooks.org/)
To extract a list of the greatest books of all time (n=300)

![](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/471b01c40da12924d810e1dd08d9c876e82c52d8/output/png/web_scraping_the_greatest_books_list.PNG)
<br> py script: [web_scraping_greatest_books.py](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/82f69120863f9d890964e995e16f823579f4a48d/src/web_scraping_greatest_books.py)
<br>
csv output: [the_greatest_books_of_all_time.csv](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/af93556c11b9368bd50a047399c35576408f22bc/output/csv/the_greatest_books_of_all_time.csv)


### Website: [en.wikipedia.org](https://en.wikipedia.org/wiki/List_of_highest-grossing_concert_tours)

To extract multiple wikipedia tables on the highest grossing concert tours of all time

![](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/dddf6808d9a33bf2a6a6377ab303e2ea74cc1948/output/png/web_scraping_highest_grossing_tours_list.PNG)
py script: [web_scraping_highest_grossing_tours.py](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/248bbff34e979778b2bb6dfdfc508aae08632250/src/web_scraping_highest_grossing_tours.py)
<br>
csv output: [top_20_highest_grossing_tours_of_all_time.csv](
https://github.com/IvoDSBarros/web-scraping-use-cases/blob/abf65f957fbf1aee00f596609344f6a605f9d4a9/output/csv/top_20_highest_grossing_tours_of_all_time.csv)

## 2. JSON var-based extraction
### Website: [www.rollingstone.com](https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/)
To extract the Rolling Stone list on the greatest albums of all time

![](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/ffc13ea89d83d9c9091c16ed9b132c91dc7695d9/output/png/web_scraping_highest_rs_album_list.PNG)
<br> py script: [web_scraping_rs_500_greatest_albums.py](https://github.com/IvoDSBarros/web-scraping-use-cases/blob/df881ee5834538e8acb4010b71c94cd879ea19e2/src/web_scraping_rs_500_greatest_albums.py)
<br>
csv output: [top_20_highest_grossing_tours_of_all_time.csv](
https://github.com/IvoDSBarros/web-scraping-use-cases/blob/abf65f957fbf1aee00f596609344f6a605f9d4a9/output/csv/top_20_highest_grossing_tours_of_all_time.csv)


## 3. JSON API-response-based extraction
### "thegreatestbooks.org"
To extract list of the greatest books of all time (n=300)

+	"en.wikipedia.org"
To extract multiple wikipedia tables on the highest grossing concert tours of all time 

