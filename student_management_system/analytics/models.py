from django.db import models
from users.models import CustomUser

from courses.models import Course


class APIRequestLog(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    status_code = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        user_display = f"User ID {self.user_id}" if self.user_id else "Anonymous User"
        return f"{user_display} requested {self.path}"


class CourseView(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)