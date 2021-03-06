from django.contrib.auth import get_user_model
from django.db import models
from rest_framework import serializers
from .models import Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username']


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    # author = AuthorSerializer()
    class Meta:
        model = Post
        fields = [
            'pk',
            'author_username',
            'message',
            'created_at',
            'is_public',
        ]

