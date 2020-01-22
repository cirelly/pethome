"""historia URL Configuration

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
from django.contrib import admin
from django.urls import include,path
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, logout_then_login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascota/', include('apps.mascota.urls', namespace='mascota')),
    path ('adopcion/', include ('apps.adopcion.urls', namespace='adopcion')),
    path ('usuario/', include ('apps.usuario.urls', namespace='usuario')),
    path('accounts/login/', LoginView.as_view(template_name= 'usuario/index.html'), name="login"),
    path('reset/password_reset', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html', 
        email_template_name='registration/password_reset_email.html'), name="password_reset"),
    path('reset/password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name="password_reset_done"),
    path('reset/password_reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
            name='password_reset_confirm'),
    path('reset/password_reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
            name='password_reset_complete'),
    path('logout/', logout_then_login, name='logout'),
]
