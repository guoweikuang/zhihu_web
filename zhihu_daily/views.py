# -*- coding: utf-8 -*-
#
# author: guoweikuang
# date: 2017-5-5
#
import logging
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from zhihu_daily.models import News
from zhihu_daily.crawl_zhihu.fetch import date_now, before_date_str, after_date_str



class IndexView(ListView):
    template_name = 'daily/index.html'
    context_object_name = 'daily_index'

    def get_queryset(self):
        """
        获取日期
        :return: 
        """

        date_str = self.kwargs['date'] if self.kwargs['date'] else date_now()
        context = {}
        try:
            news = News.objects.filter(date=date_str)
            before_date = before_date_str(date_str)
            after_date = after_date_str(date_str)
            context = {
                'news_list': news,
                'before_date': before_date,
                'after_date': after_date
            }
            return context
        except Exception as e:
            logging.error('出现错误， 错误信息为： %s' % e)
            return None

    def get_context_data(self, **kwargs):
        return super(IndexView, self).get_context_data(**kwargs)


def index(request):
    date_str = request.GET.get("date", date_now())
    context = {}
    try:
        news_list = News.objects.filter(date=date_str)

        before_date = before_date_str(date_str)
        after_date = after_date_str(date_str) \
            if date_now() != date_str else None

        context = {
            'news_list': news_list,
            'before_date': before_date,
            'after_date': after_date
        }
    except Exception as e:
        import traceback
        stack = traceback.format_exc()
        logging.error("get daily news failed date_str:%s error:%s cause:%s"
                      % (date_str, e, stack))
    else:
        return render(request, 'daily/index.html', context)


def search(request):
    keyword = request.GET.get('keyword', '')
    page = request.GET.get('page', 1)
    limit = 3

    if not keyword.strip():
        return redirect('daily/')

    try:
        news_list = News.objects.filter(title__contains=keyword)
        paginator = Paginator(news_list, limit)
        page_range = paginator.page_range
        hits = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        hits = paginator.page(page)

    except EmptyPage:
        page = paginator.num_pages
        hits = paginator.page(page)

    else:
        context = {
            'page': page,
            'page_range': page_range,
            'hits': hits,
            'keyword': keyword,
        }

        return render(request, 'daily/search.html', context)


def page_not_found_view(request):
    return render(request, '404.html')


