from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from post import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', views.PostViewSet)
router.register('album', views.ImgViewSet)
router.register('files', views.FileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
