#!/usr/bin/python
# -*- coding: utf-8 -*-

import db
import scrapy
from star import Star
from movie import Movie



DB_NAME = 'jav.db'
JAVBUS_URL = 'https://www.dmmbus.bid'
JAVLIB_URL = "http://www.n43a.com/en/"
STAR_LIST = ["紺野ひかる","三上悠亜","篠田ゆう","初川みなみ","岬ななみ","葵つかさ","明里つむぎ","橋本ありな","山岸逢花","小倉由菜","桜空もも"]

def create_new_db (db_name,javbus_url,stars):
    db.create_db(db_name)
    for s in stars:
        star_id = scrapy.get_star_javbus_code(javbus_url,s)
        print(star_id)
        star = scrapy.star_content_analyse(javbus_url,star_id)
        star.name = s
        db.insert_new_star(db_name,star)
    return

def update_db (db_name,javbus_url,javlib_url):
    star_list = db.load_stars(db_name)
    for star in star_list:
        javbus_code = star[0]
        target_url = "/star/"+javbus_code
        tmp_web = []
        rates =[]
        scrapy.load_javbus_page(javbus_url,target_url,tmp_web)
        for web in tmp_web:
            movie = scrapy.movie_content_analyse(web,javbus_code)
            search_results = scrapy.search_javlib(javlib_url,movie.code)
            for search in search_results:
                score = scrapy.get_rating(javlib_url,search)
                rates.append(int(score))
            movie.rate = max(rates)
            db.inert_new_movie(db_name,movie)
    return

create_new_db(DB_NAME,JAVBUS_URL,STAR_LIST)