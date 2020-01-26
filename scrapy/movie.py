#!/usr/bin/env python
# encoding: utf-8
'''
@author: Junkai
@license: 
@contact: bianjunkai@gmail.com
@software: Jav_Scrapy
@file: movie.py
@time: 2020/1/25 3:30 下午
@desc: Class of Movie
'''

class Movie():

    name = ''
    img = ''
    url = ''
    code = ''
    date = ''
    star_id = ''
    rate = 0


    def __init__(self, name, img, url, code, date,star_id):
        self.name = name
        self.img = img
        self.url = url
        self.code = code
        self.date = date
        self.star_id = star_id