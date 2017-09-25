# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "zhihu_web.settings"})

class News(models.Model):
    new_id = models.CharField(max_length=32)
    title = models.CharField(max_length=256)
    date = models.CharField(max_length=32)
    share_url = models.CharField(max_length=256)
    image = models.FileField(upload_to='daily/%Y-%m-%d')
    image_source = models.CharField(max_length=256)

    def __unicode__(self):
        return self.new_id

