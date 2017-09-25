# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import Celery
from datetime import timedelta


app = Celery('zhihu_daily',
             broker='redis://localhost',
             backend='redis://localhost',
             include=['zhihu_daily.tasks'])


if __name__ == '__main__':
    app.start()

