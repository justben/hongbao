from django.urls import path
from copyto import views

urlpatterns = [
    path('', views.main),
]