from django.contrib import admin
from .models import APIRequestLog
from users.models import CustomUser


class APIRequestLogAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'path', 'method', 'status_code', 'timestamp')

    def user_email(self, obj):
        if obj.user_id:
            try:
                user = CustomUser.objects.get(id=obj.user_id)
                return user.email
            except CustomUser.DoesNotExist:
                return "User Not Found"
        return "Anonymous User"

    user_email.short_description = 'User Email'

admin.site.register(APIRequestLog, APIRequestLogAdmin)
