#!/usr/bin/env python
# encoding: utf-8
'''
@author: Junkai
@license:
@contact: bianjunkai@gmail.com
@software: Jav_Scrapy
@file: scrapy.py
@time: 2020/1/25 3:38 下午
@desc: All the scrapy functions
'''

import requests
from bs4 import BeautifulSoup
from star import Star
from movie import Movie
import re


def load_page(mainURL, target_url):
    '''
    Load web page
    :param mainURL:
    :param target_url:
    :return: beautifulsoup4 content
    '''
    url = mainURL + target_url
    r = requests.get(url)
    if r.status_code == 200:
        bs = BeautifulSoup(r.content, "html.parser")
        print(r.url + " load OK")
    return bs


def load_javbus_page(javbus, target_url, web_page):
    '''
    Load one star's javbus page and recurrent for all the pages
    :param javbus: javbus web url
    :param target_url: star's page url in javbus
    :param web_page: a list for all the web items
    :return:
    '''

    bs = load_page(javbus, target_url)
    next_page = bs.find("a", id="next")
    items = bs.find_all("div", class_="item")
    for item in items:
        if item.contents[1].get("class")[0] == 'movie-box':
            web_page.append(item)

    if next_page is not None:
        next_url = next_page.get("href")
        print(next_url)
        load_javbus_page(javbus, next_url, web_page)

    return


def movie_content_analyse(item, star):
    '''
    Analyse the web data of one star
    :param item: web content of one block
    :param star: javbus code of one star
    :return: return a Movie element or nothing
    '''

    tmp_content = item.find_all("date")
    item_name = item.img.get('title')
    item_img = item.img.get('src')
    item_url = item.a.get('href')
    item_code = tmp_content[0].string
    item_date = tmp_content[1].string
    return Movie(item_name, item_img, item_url, item_code, item_date, star)


def star_content_analyse(javbus, code):
    '''
    Get the star information from Javbus
    :param javbus: javbus URL
    :param code: star code of Javbus
    :return: a star Element
    '''
    url = '/en/star/' + code
    bs = load_page(javbus, url)
    item = bs.find("div", class_="avatar-box")

    tmp_content = []
    star = dict.fromkeys(['D.O.B',
                          'Height',
                          'Cup',
                          'Bust',
                          'Waist',
                          'Hips',
                          'Hometown',
                          'Hobby'],
                         "NoValue")
    # star = {'D.O.B','Height','Cup','Bust','Waist','Hips','Hometown','Hobby'}
    for content in item.find_all("p"):
        key = content.string.split(":")[0].strip()
        value = content.string.split(":")[1].strip()
        if key in star:
            star[key] = value
            print(key + ":  " + value)

    name = item.span.string
    img = item.img.get('src')

    return Star(
        name,
        img,
        star['D.O.B'],
        star['Height'],
        star['Cup'],
        star['Bust'],
        star['Waist'],
        star['Hips'],
        star['Hometown'],
        star['Hobby'],
        code)
    # return Star(
    #     name,
    #     img,
    #     birth_date,
    #     height,
    #     cup,
    #     bust,
    #     waist,
    #     hip,
    #     birth_place,
    #     hobby,
    #     code)


def get_star_javbus_code(javbus, name):
    '''
    Get the star's Javbus code
    :param javbus: javbus url
    :param name: name of star
    :return: code
    '''
    searchurl = "/searchstar/" + name
    bs = load_page(javbus, searchurl)
    star_box = bs.find_all("a", class_="avatar-box")
    for result in star_box:
        href = result.get("href")
        star_title = result.find("img").get("title")
        if star_title == name:
            return href.split("/").pop()


def search_javlib(javlib, code):
    '''
    Get the search result from javlib
    :param javlib: javlib url
    :param code: movie code
    :return: all the links to the video
    '''
    search_url = "/vl_searchbyid.php?keyword=" + code
    bs = load_page(javlib, search_url)
    pattern = re.compile('ID Search Result')
    text = bs.title.string
    match = pattern.search(text)
    print(match)
    video_urls = []
    if match is not None:

        items = bs.find_all("div", class_="video")
        for item in items:
            if item.find(class_="id").string == code:
                video_url = item.a.get("href").split("/").pop()
                video_urls.append(video_url)
    else:

        item = bs.find(id="video_title")
        video_url = item.a.get("href").split("/").pop()
        video_urls.append(video_url)

    return video_urls


def get_rating(javlib, target_url):
    '''
    Return the rating score from javlib
    :param javlib:
    :param target_url:
    :return:
    '''
    pattern = re.compile(r'[(](.*?)[)]', re.S)
    bs = load_page(javlib, target_url)
    score = bs.find("span", class_="score").string
    if score:
        score = re.findall(pattern, score)[0]
    else:
        score = "0.0"
    print("Movie Score: " + score)
    return score


# def get_rating_javlib(javlib,name):
#
#     load_page(javlib,)
# search_javlib("http://www.n43a.com/en/","mizd-095")
print(search_javlib("http://www.n43a.com/en/", "MMUS-004"))
# get_rating("http://www.n43a.com/en/","?v=javli7di2a")
# a = get_star_javbus_code("https://www.dmmbus.bid","初川みなみ")
# print(a)
#star = star_content_analyse("https://www.dmmbus.bid/en","okq")
#a = []
# load_javbus_page("https://www.dmmbus.bid",'/star/qs6/',a)
#i = 0
# for web in a :
#     for item in web:

#        movie = movie_content_analyse(item,'qs6')
#       if movie != None:
##         i += 1
