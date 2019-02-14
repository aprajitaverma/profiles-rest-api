from django.shortcuts import render

from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions
from rest_framework import status

# Create your views here.


class HelloAPIView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTPmethods as function (get, post, patch, pur, delete)',
            'It is similar to traditional django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message' : 'Hey there!', 'an_apiview' : an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method' : 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method' : 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        return Response({'method' : 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewset."""

    serializer_class = serializers.HelloSerializers

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'User actions (list, create, retrieve update, partial_update)',
            'Automatically maps to URLs using Routers.',
            'Provides more functionality with less code.'
        ]

        return Response({'message' : 'Hello There!', 'a_viewset' : a_viewset})

    def create(self, request):
        """Create a new hello string."""

        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method' : 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method' : 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method' : 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method' : 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating models"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken API View to validate and create token."""

        return ObtainAuthToken().post(request)
