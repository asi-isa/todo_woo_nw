from django.urls import path

from . import views

urlpatterns = [
    path('', views.signup_user, name='signup_user'),

]