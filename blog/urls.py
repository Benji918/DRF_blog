from django.urls import include, path
from .views import BlogViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blog', BlogViewSets)

app_name = 'blogs'

urlpatterns = [
    path('', include(router.urls)),
]

