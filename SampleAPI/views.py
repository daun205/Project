from django.shortcuts import render

from django.contrib.auth.models import User, Group
from .models import (Post)
from SampleAPI.serializers import UserSerializer, GroupSerializer, PostSerializer


from rest_framework import viewsets
from rest_framework.authentication import (SessionAuthentication, 
    BasicAuthentication,TokenAuthentication)
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)   

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]