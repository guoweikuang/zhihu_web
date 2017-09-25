# -*- coding: utf-8 -*-
"""
抓取知乎日报API内容
"""
import json
import time

from django.core.management.base import BaseCommand

from zhihu_daily.crawl_zhihu import zhihu
from zhihu_daily.crawl_zhihu import fetch
from zhihu_daily.models import News

def save_data():
    zhi = zhihu.Zhihu()
    latest_news = zhi.get_latest_news()
    print(json.dumps(latest_news, ensure_ascii=False, indent=2))

    latest_news_id = fetch.extract_news_id(latest_news)
    date = latest_news['date']

    for new_id in latest_news_id:
        content = zhi.get_news_by_new_id(new_id)
        image_name, image = fetch.get_image_data(content['image'])
        new_obj, _ = News.objects.get_or_create(
            new_id=new_id,
            title=content['title'],
            date=date,
            share_url=content['share_url'],
            image_source=content['image_source'] if content['image_source'] else ''
        )
        new_obj.image.save(image_name, image)


class Command(BaseCommand):
    help = 'saving api content to database'

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--cron',
            action='store_true',
            dest='cron',
            default=False,
            help=u'定时任务'
        )
        # parser.add_argument('date', type=int)
        parser.add_argument('days', type=int)

    def handle(self, *args, **options):
        self.save_data()
        if options.get('cron'):
            self.cron_run_fetch()

        # if options.get('date'):
        #     self.save_before_date(options.get('date'))

        if options.get('days'):
            self.save_more_news(options.get('days'))

    def save_data(self):
        zhi = zhihu.Zhihu()
        latest_news = zhi.get_latest_news()
        print(json.dumps(latest_news, ensure_ascii=False, indent=2))

        latest_news_id = fetch.extract_news_id(latest_news)
        date = latest_news['date']

        for new_id in latest_news_id:
            content = zhi.get_news_by_new_id(new_id)
            image_name, image = fetch.get_image_data(content['image'])
            try:
                image_source = content['image_source']
            except:
                image_source = ''
            new_obj, _ = News.objects.get_or_create(
                new_id=new_id,
                title=content['title'],
                date=date,
                share_url=content['share_url'],
                image_source=image_source
            )
            new_obj.image.save(image_name, image)

    def save_before_date(self, date):
        zhi = zhihu.Zhihu()
        latest_news = zhi.get_news_before_now(date)
        # print(json.dumps(latest_news, ensure_ascii=False, indent=2))

        latest_news_id = fetch.extract_news_id(latest_news)
        date = latest_news['date']

        for new_id in latest_news_id:
            content = zhi.get_news_by_new_id(new_id)
            image_name, image = fetch.get_image_data(content['image'])
            new_obj, _ = News.objects.get_or_create(
                new_id=new_id,
                title=content['title'],
                date=date,
                share_url=content['share_url'],
                image_source=content['image_source']
            )
            new_obj.image.save(image_name, image)

    def save_more_news(self, days):
        date_now = fetch.date_now()
        dates = []
        for i in range(days):
            dates.append(date_now)
            date_now = fetch.before_date_str(date_now)
        print(dates)
        for date in dates:
            self.save_before_date(date)

    def cron_run_fetch(self):
        interval_hour = 2
        while 1:
            try:
                self.save_data()
            except Exception as e:
                pass
            time.sleep(interval_hour * 3600)









