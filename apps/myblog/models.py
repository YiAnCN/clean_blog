from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from django.utils.html import mark_safe
from markdown import markdown
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')


class Post(models.Model):
    title = models.CharField(max_length=20, verbose_name=u'标题')
    author = models.ForeignKey(User, verbose_name=u'作者')
    body = models.TextField(verbose_name=u'文章内容')
    image = models.ImageField(upload_to='picture/%Y/%m', max_length=100, verbose_name='对应图片')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')
    updated = models.DateTimeField(auto_now=True,verbose_name=u'更新时间')
    status = models.CharField(max_length=10,
                              choices=(('Essays', '随笔'), ('Feelings', '感想'), ('Notes', '笔记')),
                              verbose_name='归类')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.


    class Meta:
        verbose_name = u'文章信息'
        verbose_name_plural = verbose_name
        ordering = ('-add_time',)

    def __str__(self):
        return self.title


    def get_body_as_markdown(self):
        return mark_safe(markdown(self.body, safe_mode='escape'))




