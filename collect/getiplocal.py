from django.test import TestCase

# Create your tests here.

class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)
        return response


    def process_view(self, request, view_func, *view_args, **view_kwargs):
        EXCLUDE_IPS = ['192.168.1.54']
        if 'HTTP_X_FORWARDED_FOR' in  request.META:
            ip =  request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        print(ip)
        if ip in EXCLUDE_IPS:
            return HttpResponse()
        return None