#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from zhihu_daily.celery import app
#from zhihu_daily.crawl_zhihu.zhihu import Zhihu
from zhihu_daily.management.commands.fetch_zhihu import *
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

engine = create_engine('sqlite:///{}/db.sqlite3'.format(BASE_DIR), echo=True)
metadate = MetaData(engine)
Base = declarative_base()


#class News(Base):
#    __tablename__ = 'zhihu_daily_news'
#    new_id = 23

@app.task
def add(x, y):
    return x + y


@app.task
def fetch_zhihu():
    save_data()
