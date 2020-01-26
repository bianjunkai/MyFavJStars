# MyFavJStarts

** A crawler based on python (requests+beautifulsoup). **

The * main purpose * is try to crawl www.javbus.com and www.javlibrary.com to scrapy the movie metadata.

## There are three paramaters need to be predefined:
URL of Javbus : the url should be used without proxy
URL of Javlibrary : the url should be used without proxy
List of Star: the list of star that wanted to be followed

## The workflow is 
1.  create db (sqlite3) and create table star and table movie
2.  update all the information of stars and then store in the db
3.  load the star information and crawl all movies belong to this star from javbus
4.  get the rating data from Javlibray and store the movie data into db.

## TODO 1: UI design:
The next main mission is to create a Web UI linked to the DB.
The Web will complete these missions :
1. Give a global view of the db;
2. Show the list of stars;
2. Show the movie list of each star : name,code,url,rating,etc.
3. Show the best magnet link of the movie to download
4. Record the status of the movie: Like,Downloaded,Ignore

## TODO 2: Crawler 
The next main mission is to optimize the crawler.
1. Do not crawl all the data if the data existed then finish the job.
2. Get and analyse the magnet link then record the best one.
3. Multi-process and cycle task


