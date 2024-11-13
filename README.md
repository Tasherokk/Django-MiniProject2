# Django-MiniProject2
# Student Management System

# To Start Celery Workers and Beat: <br>
celery -A student_management_system worker -l info <br>
celery -A student_management_System beat -l info

# To Start Redis
cd C:\Redis <br>
redis-server.exe

# To Generate analytics
python manage.py generate_analytics

# To Start Unit Test
python manage.py test