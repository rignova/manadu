from django.shortcuts import render


def setup(request):
    template = 'setup/setup.html'
    return render(request, template)
