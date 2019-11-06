
from django.urls import path
from account import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup_confirmation/',views.SignUpConfirmationView.as_view(),name='signup_confirmation'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('invalid_activate/', views.InvalidActivation.as_view(), name='invalid_activate'),
    path('signup_activation_done/', views.SignUpActivationDone.as_view(), name='signup_activation_done'),

]