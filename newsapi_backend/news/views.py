from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class NewsAPIView(APIView):
    def get(self, request, format=None):
        query = request.GET.get('query', '')
        category = request.GET.get('category', '')
        apiKey = '7bfdd61741ad4abf949c3cd11203440d'
        
        url = f'https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey={apiKey}'
        
        if query:
            url = f'https://newsapi.org/v2/everything?q={query}&domains=techcrunch.com,thenextweb.com&apiKey={apiKey}'
        
        if category:
            url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={apiKey}'
            if query:
                url += f'&q={query}'
        
        response = requests.get(url)
        return Response(response.json())

