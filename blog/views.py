from .permissions import IsOwnerOfStudent
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import BlogSerializer
from core.models import BlogPost
from rest_framework import viewsets


class BlogViewSets(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOfStudent]

    def get_queryset(self):
        """Return only Blog objects for the request user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        """Create a new Blogs for specific authenticated user"""
        return serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """Update an existing Blog for the specific authenticated user"""
        serializer.save(user=self.request.user)

    