from django.shortcuts import render,get_object_or_404
from django.views.generic.base import View
from .models import Post
from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class IndexView(View):
    def get(self,request):
        posts = Post.objects.all().order_by("-add_time")


        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(posts, 3, request=request)
        post = p.page(page)
        return render(request,'index.html',{
            'posts': post,


        })


class ContactView(View):
    def get(self,request):
        return render(request,'contact.html',{})





class SingleView(View):
    def get(self,request,title_id):
        post = Post.objects.get(id=int(title_id))

        return render(request,'single.html',{
            'post':post,

        })
