from django.test import TestCase

# Create your tests here.

class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)
        return response


    def process_view(self, request, view_func, *view_args, **view_kwargs):
        EXCLUDE_IPS = ['8.210.10.46','165.227.47.218','167.94.138.52','114.132.203.195'
,'61.241.56.179','65.49.1.102']
        if 'HTTP_X_FORWARDED_FOR' in  request.META:
            ip =  request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        print(ip)
        if ip in EXCLUDE_IPS:
            print("No connect.")
            return HttpResponse()
        return None