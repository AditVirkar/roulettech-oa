from django.urls import path
from .views import NewsAPIView

urlpatterns = [
    path('api/news/', NewsAPIView.as_view(), name='news-api'),
]
