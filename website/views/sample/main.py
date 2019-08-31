from django.http import HttpResponse


def web_home(request):
    return HttpResponse('Hello Manadu!')
