from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter

from .views import (
	PostViewSet,
	UserViewSet,
	GroupViewSet
	)

router = DefaultRouter()

router.register(r'posts', PostViewSet, base_name='post')
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)

api_urls = router.urls