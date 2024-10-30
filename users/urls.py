from django.urls import path
from .views import UserCreateView
from .views import UserLoginApiView,UserLogoutView,UserListApiView,SSLCommerzInitiatePayment,PaymentSuccessView

urlpatterns = [
    path('',UserListApiView.as_view(),name='users'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='api-login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('payment/', SSLCommerzInitiatePayment.as_view(), name='sslcommerz_initiate'),
    path('payment/success/<int:id>/', PaymentSuccessView.as_view(), name='payment'),
]