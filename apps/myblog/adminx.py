# _*_ coding: utf-8 _*_
__author__ = 'williams_z'
__data__ = '2018/3/13 20:58'

import xadmin
from xadmin import views

from .models import Post

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = 'williams_z的个人博客'
    site_footer = '个人博客'
    menu_style = 'accordion'

class PostAdmin(object):
    list_display = ['title', 'author', 'body','image','add_time','updated','status']
    search_fields = ['title', 'author', 'body','image','add_time','updated','status']
    list_filter = ['title', 'author', 'body','image','add_time','updated','status']

xadmin.site.register(Post, PostAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)