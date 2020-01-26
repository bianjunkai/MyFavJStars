#!/usr/bin/env python
# encoding: utf-8
'''
@author: Junkai
@license:
@contact: bianjunkai@gmail.com
@software: Jav_Scrapy
@file: db.py
@time: 2020/1/24 10:15 上午
@desc: Create DB and Provide db functions
'''

import sqlite3
from star import Star
from movie import Movie


def create_db(db_name):
    '''
    Create sqllite3 db file.
    :param db_name: name of db files
    :return:
    '''
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS STAR ( id	TEXT,name	TEXT,en_name    TEXT,img	TEXT,d_o_b	TEXT,height	TEXT,cup	TEXT,bust	TEXT,waist	TEXT,hip	TEXT,hometown	TEXT,hobby	TEXT)')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS MOVIE (name	TEXT,img	TEXT,url	TEXT,code	TEXT,date	TEXT,star_id	TEXT,status	INTEGER,rate REAL);')
    cursor.close()
    connection.commit()
    connection.close()
    return


def load_stars(db_name):
    '''
    Return all the stars from db
    :param db_name:
    :return: all the stars id exited in db
    '''
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    sql = 'SELECT id,name from STAR'
    cursor.execute(sql)
    values = cursor.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return values


def load_info_of_star(db_name, star_id):
    '''
    Get all the information of one star
    :param db_name:
    :param star_id:
    :return: all the information of one star
    '''
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    sql = 'SELECT * from STAR where id =?'
    cursor.execute(sql, (star_id,))
    values = cursor.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return values


def load_movies_of_star(db_name, star_id):
    '''
    Get the one star's all mvoies
    :param db_name:
    :param star_id:
    :return: rowid and movie code
    '''
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    sql = 'SELECT rowid,code from MOVIE where star_id =?'
    cursor.execute(sql, (star_id,))
    values = cursor.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return values


def load_movie_info(db_name, movie_rowid):
    '''
    Get all the information of one movie
    :param db_name:
    :param movie_rowid:
    :return: all information of one movie
    '''
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    sql = 'SELECT * from MOVIE where rowid =?'
    cursor.execute(sql, (movie_rowid,))
    values = cursor.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return values


def insert_new_star(db_name, star):
    '''
    Insert star information into db
    :param db_name:
    :param star:
    :return:
    '''
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    data = (
        star.code,
        star.name,
        star.en_name,
        star.img,
        star.d_o_b,
        star.height,
        star.cup,
        star.bust,
        star.waist,
        star.hip,
        star.hometown,
        star.hobby)
    print(data)
    sql = 'insert into STAR (id,name,en_name,img,d_o_b,height,cup,bust,waist,hip,hometown,hobby) values (?,?,?,?,?,?,?,?,?,?,?,?)'
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    return


def inert_new_movie(db_name, movie):
    '''
    Intser movie information into db
    :param db_name:
    :param movie:
    :return:
    '''
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    data = (
        movie.name,
        movie.img,
        movie.url,
        movie.code,
        movie.date,
        movie.star_id,
        '0',
        movie.rate)
    sql = 'insert into MOVIE (name,img,url,code,date,star_id,status,rate) values (?,?,?,?,?,?,?,?)'
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    return


# a = Movie('12', '23', '45', '67', '89', '100', '101',)
# inert_new_movie('test.db',a)
#
