from .models import APIRequestLog

class APILogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if request.user.is_authenticated:
            APIRequestLog.objects.create(
                user_id=request.user.id,
                path=request.path,
                method=request.method,
                status_code=response.status_code
            )

        return response
