from scraper.views import get_home, get_news
from django.urls import path

urlpatterns = [
    path('news/', get_news),
    path('', get_home)
]