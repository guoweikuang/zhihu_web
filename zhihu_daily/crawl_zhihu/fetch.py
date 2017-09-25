# -*- coding: utf-8 -*-
"""
知乎日报 
"""
import datetime
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


def date_now():
    """ 当前时间 """
    return datetime.datetime.now().strftime('%Y%m%d')


def before_date_str(date):
    """ 当前时间的前一天 """
    now_date = datetime.datetime.strptime(date, '%Y%m%d')
    before_date = now_date - datetime.timedelta(days=1)
    print(before_date.strftime('%Y%m%d'))
    return before_date.strftime('%Y%m%d')


def after_date_str(date):
    """ 当前时间的后一天 """
    now_date = datetime.datetime.strptime(date, '%Y%m%d')
    after_date = now_date + datetime.timedelta(days=1)

    return after_date.strftime('%Y%m%d')


def extract_news_id(news):
    """ 提取最新新闻id """
    news_id = []
    all_new = news['stories']
    for new in all_new:
        new_id = new['id']
        news_id.append(new_id)
    return news_id


def get_image_data(image_url):
    """ 抓取图片 """
    content = requests.get(image_url, stream=True)
    if content.status_code == 200:
        img_name = image_url.split('/')[-1]
        img_temp = NamedTemporaryFile()
        img_temp.write(content.content)
        img_temp.flush()
        return img_name, File(img_temp)
    else:
        return None, None



