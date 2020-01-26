#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class Movie():

    name = ''
    img = ''
    url = ''
    code = ''
    date = ''

    def __init__(self, name, img, url, code, date):
        self.name = name
        self.img = img
        self.url = url
        self.code = code
        self.date = date


class Star():
    name = ''
    img = ''
    birth_date = ''
    height = ''
    cup = ''
    bust = ''
    waist = ''
    hip = ''
    birth_place = ''
    hobby = ''

    def __init__(self, name, img, birth_date, height, cup,
                 bust, waist, hip, birth_place, hobby):
        self.name = name
        self.img = img
        self.birth_date = birth_date
        self.height = height
        self.cup = cup
        self.bust = bust
        self.waist = waist
        self.hip = hip
        self.birth_place = birth_place
        self.hobby = hobby


URL = 'https://www.dmmbus.bid'
CUR = '/star/mj2/'
movies = []
star = Star('', '', '', '', '', '', '', '', '', '')


def loadpage(URL, CUR):
    url = URL + CUR
    print(url)
    r = requests.get(url)
    bs = BeautifulSoup(r.content, "html.parser")
    next_page = bs.find("a", id="next")
    items = bs.find_all("div", class_="item")

    for item in items:
        if item.contents[1].get("class")[0] == 'movie-box':
            movieContentTrans(item)
        elif item.contents[1].get("class")[0] == 'avatar-box':
            s = starContentTrans
            if s is not None:
                star = s

    if next_page is not None:
        next_url = next_page.get("href")
        loadpage(URL, next_url)

    return star

# item = items[0]


def movieContentTrans(item):
    tmp_content = item.find_all("date")
    item_name = item.img.get('title')
    item_img = item.img.get('src')
    item_url = item.a.get('href')
    item_code = tmp_content[0].string
    item_date = tmp_content[1].string
    movie = Movie(item_name, item_img, item_url, item_code, item_date)
    movies.append(movie)
    print(item_code)
    return


def starContentTrans(item):
    tmp_content = []
    for content in item.find_all("p"):
        tmp_content.append(content.string)

    name = item.span.string
    img = item.img.get('src')
    birth_date = tmp_content[0]
    height = tmp_content[2]
    cup = tmp_content[3]
    bust = tmp_content[4]
    waist = tmp_content[5]
    hip = tmp_content[6]
    birth_place = tmp_content[7]
    hobby = tmp_content[8]

    star = Star(
        name,
        img,
        birth_date,
        height,
        cup,
        bust,
        waist,
        hip,
        birth_place,
        hobby)

    return star


star = loadpage(URL, CUR)
print(star.name, star.hobby)
for m in movies:
    print(m.code)
