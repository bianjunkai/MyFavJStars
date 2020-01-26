#!/usr/bin/env python
# encoding: utf-8
'''
@author: Junkai
@license: 
@contact: bianjunkai@gmail.com
@software: Jav_Scrapy
@file: star.py
@time: 2020/1/25 2:53 下午
@desc: Class of Star
'''

class Star():
    name = ''
    en_name = ''
    img = ''
    d_o_b = ''
    height = ''
    cup = ''
    bust = ''
    waist = ''
    hip = ''
    hometown = ''
    hobby = ''
    code =''

    def __init__(self, en_name, img, d_o_b, height, cup,
                 bust, waist, hip, hometown, hobby,code):
        self.name = 'name'
        self.en_name = en_name
        self.img = img
        self.d_o_b = d_o_b
        self.height = height
        self.cup = cup
        self.bust = bust
        self.waist = waist
        self.hip = hip
        self.hometown = hometown
        self.hobby = hobby
        self.code = code
