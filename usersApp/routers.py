from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from .views import UserViewSet


router = DefaultRouter()

router.register('', UserViewSet)
urlpatterns = router.urls;