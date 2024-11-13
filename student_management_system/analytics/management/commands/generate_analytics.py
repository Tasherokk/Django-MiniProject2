from django.core.management.base import BaseCommand
from analytics.models import APIRequestLog
from django.contrib.auth import get_user_model
from django.db.models import Count

from analytics.models import CourseView

User = get_user_model()

class Command(BaseCommand):
    help = 'Generate analytics reports'

    def handle(self, *args, **kwargs):
        user_activity = (
            APIRequestLog.objects
            .values('user_id')
            .annotate(request_count=Count('id'))
            .order_by('-request_count')
        )

        self.stdout.write("Most Active Users:")
        for activity in user_activity:
            user_id = activity['user_id']
            request_count = activity['request_count']
            try:
                user_email = User.objects.get(id=user_id).email if user_id else "Anonymous"
                self.stdout.write(f"{user_email}: {request_count} requests")
            except User.DoesNotExist:
                self.stdout.write(f"User ID {user_id} not found: {request_count} requests")

        self.stdout.write('\nMost Popular Courses:')
        popular_courses = (
            CourseView.objects.values('course__name')
            .annotate(view_count=Count('id'))
            .order_by('-view_count')[:10]
        )

        for course in popular_courses:
            self.stdout.write(f"{course['course__name']}: {course['view_count']} views")