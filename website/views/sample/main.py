from django.shortcuts import render


def web_home(request):
    template = 'sample/index.html'
    return render(request, template)
