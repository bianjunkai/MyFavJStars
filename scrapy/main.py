#!/usr/bin/python
# -*- coding: utf-8 -*-

import db
import scrapy
from star import Star
from movie import Movie


DB_NAME = 'jav.db'
JAVBUS_URL = 'https://www.dmmbus.bid'
JAVLIB_URL = "http://www.n43a.com/en/"
STAR_LIST = [
    "紺野ひかる",
    "三上悠亜",
    "篠田ゆう",
    "初川みなみ",
    "岬ななみ",
    "葵つかさ",
    "明里つむぎ",
    "橋本ありな",
    "山岸逢花",
    "小倉由菜",
    "桜空もも"]


def create_new_db(db_name, javbus_url, stars):
    '''
    Create a new db file with 2 tables
    :param db_name:
    :param javbus_url:
    :param stars:
    :return:
    '''
    db.create_db(db_name)
    for s in stars:
        star_id = scrapy.get_star_javbus_code(javbus_url, s)
        print(star_id)
        star = scrapy.star_content_analyse(javbus_url, star_id)
        star.name = s
        db.insert_new_star(db_name, star)
    return


def scan_newest_data(db_name, javbus_url, javlib_url):
    '''
    Scan the newest data use for daily time
    :param db_name:
    :param javbus_url:
    :param javlib_url:
    :return:
    '''
    star_list = db.load_stars(db_name)
    print(star_list)
    for star in star_list:
        print(star[1])
        javbus_code = star[0]
        target_url = "/star/" + javbus_code
        tmp_web = []
        movie_exists = db.load_movies_of_star(db_name, javbus_code)
        print(movie_exists)
        scrapy.load_new_javbus_page(
            javbus_url, target_url, tmp_web, movie_exists)
        if tmp_web:
            movie = scrapy.generate_movies_from_webblob(
                tmp_web, javbus_code, javlib_url)
            db.inert_new_movie(db_name, movie)
    return


def scan_all_data(db_name, javbus_url, javlib_url):
    '''
    Scan all the movie data for the db,usually used for the empty db
    :param db_name:
    :param javbus_url:
    :param javlib_url:
    :return:
    '''
    star_list = db.load_stars(db_name)
    print(star_list)
    for star in star_list:
        print(star[1])
        javbus_code = star[0]
        target_url = "/star/" + javbus_code
        tmp_web = []
        scrapy.load_all_javbus_page(javbus_url, target_url, tmp_web)
        # print(tmp_web)
        # for web in tmp_web:
        #     rates = []
        #     movie = scrapy.movie_content_analyse(web, javbus_code)
        #     print(movie.code)
        #     search_results = scrapy.search_javlib(javlib_url, movie.code)
        #     if search_results:
        #         for search in search_results:
        #             print("Search Results: " + search)
        #             score = scrapy.get_rating(javlib_url, search)
        #             print(score)
        #             rates.append(float(score))
        #     else:
        #         print("Not Found")
        #         rates.append(0.0)
        #     print(rates)
        #     movie.rate = max(rates)
        #     print(movie.rate)
        if tmp_web:
            movie = scrapy.generate_movies_from_webblob(
                tmp_web, javbus_code, javlib_url)
            db.inert_new_movie(db_name, movie)
    return


# create_new_db(DB_NAME,JAVBUS_URL,STAR_LIST)
scan_newest_data(DB_NAME, JAVBUS_URL, JAVLIB_URL)
# scrapy.load_javbus_page('https://www.dmmbus.bid',"/star/93l/15",[])
