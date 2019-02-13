from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloAPIView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
        'Uses HTTPmethods as function (get, post, patch, pur, delete)',
        'It is similar to traditional django view',
        'Gives you the most control over your logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message' : 'Hey there!', 'an_apiview' : an_apiview})
