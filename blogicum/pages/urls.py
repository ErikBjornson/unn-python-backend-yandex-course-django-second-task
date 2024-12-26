from django.urls import path

from .views import about, rules


app_name = 'pages'

urlpatterns = [
    path(
        route='about/',
        view=about,
        name='about',
    ),
    path(
        route='rules/',
        view=rules,
        name='rules',
    ),
]
