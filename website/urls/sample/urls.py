from django.urls import path
from website.views.sample.main import web_home

urlpatterns = [
    path('', web_home, name='web_home'),
]
