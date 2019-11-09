from django.urls import path
from .views import home, webhook

urlpatterns = [
    path('', home, name='home'),
    path('webhook/', webhook, name='webhook'),
]
