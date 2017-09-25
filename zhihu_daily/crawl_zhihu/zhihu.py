# -*- coding: utf-8 -*-
"""
知乎日报 API 接口
"""
import logging
import json
import requests

logging.basicConfig(filename='api.log', format="%(asctime)s %(levelname)s:%(message)s", level=logging.DEBUG)


class Zhihu(object):
    def __init__(self):
        self.host = 'http://news-at.zhihu.com'
        self.timeout = 10
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/58.0.3029.81 Safari/537.36',
        }

    def get_latest_news(self):
        """ 获取最新新闻 """
        content = self._get_api_content('/api/4/news/latest')
        return json.loads(content)

    def get_news_by_new_id(self, new_id):
        """ 获取新闻new_id的内容 """
        content = self._get_api_content('/api/3/news/%s' % new_id)
        return json.loads(content)

    def get_news_before_now(self, date):
        content = self._get_api_content('/api/3/news/before/%s' % date)
        return json.loads(content)

    def _get_api_content(self, url):
        """ 抓取url的内容 """
        print('=====>：', url)
        url = self.host + url
        print(url)
        content = ''
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                content = response.content
            else:
                error = response.status_code
                print('=====> error:', error)
                logging.error('api获取出现错误，错误标识为：%s' % error)
        except Exception as e:
            logging.error('出现错误，错误信息为：%s' % e)
            print(u'出现错误， ', e)
        return content.decode('utf-8')
