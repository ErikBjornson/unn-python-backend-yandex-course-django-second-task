from django.urls import path

from .views import (
    index,
    post_detail,
    category_posts,
)

app_name = 'blog'

urlpatterns = [
    path(
        route='',
        view=index,
        name='index',
    ),
    path(
        route='posts/<int:post_id>/',
        view=post_detail,
        name='post_detail',
    ),
    path(
        route='category/<slug:category_slug>/',
        view=category_posts,
        name='category_posts',
    ),
]
