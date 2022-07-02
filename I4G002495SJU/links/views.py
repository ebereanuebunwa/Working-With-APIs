from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import LinkSerializer
from .models import Link


# Create your views here.
class PostListApi(ListAPIView):  
    queryset = Link.objects.filter(active=True)  
    serializer_class = LinkSerializer  


class PostCreateApi(CreateAPIView):  
    queryset = Link.objects.filter(active=True)  
    serializer_class = LinkSerializer


class LinkUpdateApi(UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class LinkDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer




