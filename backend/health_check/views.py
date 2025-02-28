from django.http import HttpResponse

def health_check(request):
    return HttpResponse(status=200)