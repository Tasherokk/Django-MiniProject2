from rest_framework.routers import DefaultRouter
from .views import APIRequestLogViewSet

router = DefaultRouter()
router.register(r'analytics', APIRequestLogViewSet, basename='analytics')

urlpatterns = router.urls
