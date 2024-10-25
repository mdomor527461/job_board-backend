from django.urls import path
from .views import UserCreateView
from .views import UserLoginApiView,UserLogoutView,UserListApiView

urlpatterns = [
    path('',UserListApiView.as_view(),name='users'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='api-login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]