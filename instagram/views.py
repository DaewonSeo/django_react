from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from typing_extensions import ParamSpecArgs
from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

#genrics를 상속 받아서 구현하는 방법
# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

# APIView로 직접 구현하는 방법
# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)

#장식자를 활용하여 함수로 직접 구현하는 방법
@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def dispatch(self, request, *args, **kwargs):
    #     print("requst.body:", request.body)
    #     print("reques.POST:", request.POST)
    #     return super().dispatch(request, *args, **kwargs)

# def post_list(request):
#     pass

# def post_detail(request, pk):
#     pass

