from django.shortcuts import render, get_object_or_404,render_to_response
from django.http import HttpResponse
from .models import Article, BlogType

# Create your views here.
def Hello(request):
    return HttpResponse("<h1>hello world!</h1>")


def detail(request, article_id):
    context = {}
    context['article'] = get_object_or_404(Article, pk=article_id)
    return render_to_response("blog_detail.html", context)

def base(request):
    context =  {}
    return render_to_response("base.html", context)

def blog_list(request):
    context =  {}
    context['blogs'] = Article.objects.all()
    return render_to_response("blog_list.html", context)
