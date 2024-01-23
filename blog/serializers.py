from rest_framework import serializers
from core.models import BlogPost


class BlogSerializer(serializers.ModelSerializer):
    # Additional field for the username
    author = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author']

    def get_author(self, obj):
        # Return the username of the user associated with the BlogPost
        return obj.user.username
