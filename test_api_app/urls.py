from django.urls import path

from test_api_app import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
