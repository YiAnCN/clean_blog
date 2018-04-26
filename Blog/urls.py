"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from myblog.views import IndexView,ContactView,SingleView
from django.views.static import serve
from Blog.settings import MEDIA_ROOT

import xadmin


urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^index/',IndexView.as_view(),name = 'index'),
    url(r'^media/(?P<path>.*)/$',serve,{"document_root":MEDIA_ROOT}),
    url(r'^contact/$',ContactView.as_view(),name = 'contact'),
    url(r'^single/(?P<title_id>\d+)/$',SingleView.as_view(),name = 'single'),

]
