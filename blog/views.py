import time

from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from .models import BlogPost


@cache_page(60 * 15)
def post_view(request, post_id):
    time.sleep(5)
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, "blog_post.html", {"post": post})
