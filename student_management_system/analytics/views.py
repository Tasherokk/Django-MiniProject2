from rest_framework import viewsets
from .models import APIRequestLog
from .serializers import APIRequestLogSerializer
from users.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

class APIRequestLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View to list and retrieve API request logs.
    Accessible only to authenticated admin users.
    """
    queryset = APIRequestLog.objects.all()
    serializer_class = APIRequestLogSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(
        operation_description="Retrieve all API request logs",
        responses={200: APIRequestLogSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        """
        Returns a list of all API request logs.
        Only accessible to authenticated admin users.
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve a specific API request log by its ID",
        responses={200: APIRequestLogSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        """
        Returns the details of a specific API request log.
        """
        return super().retrieve(request, *args, **kwargs)