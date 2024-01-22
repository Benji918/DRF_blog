from rest_framework import serializers
from core.models import BlogPost


class BlogSerializer(serializers.Serializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author']
        read_only_fields = ['id']
