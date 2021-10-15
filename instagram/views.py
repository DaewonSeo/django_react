from typing_extensions import ParamSpecArgs
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

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

