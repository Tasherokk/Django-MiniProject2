from rest_framework import serializers
from .models import APIRequestLog

class APIRequestLogSerializer(serializers.ModelSerializer):
    """
    Serializer for logging details of API requests.
    """
    timestamp = serializers.DateTimeField(help_text="The date and time when the request was made.")
    path = serializers.CharField(help_text="The URL path accessed during the request.")
    method = serializers.CharField(help_text="HTTP method used (GET, POST, etc.).")
    response_code = serializers.IntegerField(help_text="The HTTP response code returned.")

    class Meta:
        model = APIRequestLog
        fields = '__all__'