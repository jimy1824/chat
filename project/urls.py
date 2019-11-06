"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account import forms
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('', include('chat.urls')),
    path('account',include('account.urls')),
    path('login/', auth_views.LoginView.as_view( template_name="login.html", authentication_form=forms.UserLoginForm),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset_form.html",form_class=forms.EmailValidationOnForgotPassword,email_template_name='password_reset_email.html'),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path('reset/<str:uidb64>/<str:token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html",form_class=forms.CustomSetPasswordForm),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
