from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from scraper.api import init

from scraper.models import News
from scraper.serializer import NewsSerializer

@api_view(['GET'])
def get_news(request):
    news = News.objects.all()
    
    if len(news) == 0:
        init()
        news = News.objects.all()
    
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_home(request):
    return Response({"message": "The home"})