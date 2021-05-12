from django.urls import path, include

from rest_framework.routers import DefaultRouter

from test_api_app import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
