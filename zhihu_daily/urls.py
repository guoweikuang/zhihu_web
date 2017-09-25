from django.conf.urls import url
from zhihu_daily import views


urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    url(r'search/$', views.search, name='search'),
]