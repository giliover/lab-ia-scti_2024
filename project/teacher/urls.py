
from . import views
from django.urls import path


urlpatterns = [
    path('hello/', views.hello_teacher, name='hello_teacher'),
]
