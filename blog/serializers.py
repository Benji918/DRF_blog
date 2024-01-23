from rest_framework import serializers
from core.models import BlogPost


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id']
