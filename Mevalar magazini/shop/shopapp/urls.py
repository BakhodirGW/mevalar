from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('sent_message/', views.sent_message, name='sent_message'),
    path('chizma/', views.chizma, name='chizma')
]