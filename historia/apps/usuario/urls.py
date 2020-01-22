from django.urls import path, include
from apps.usuario.views	import RegistroUsuario, UserAPI
from django.contrib.auth.views import LoginView

app_name = "usuario"
urlpatterns = [
     path('registrar', RegistroUsuario.as_view(), name='registrar'),
     path('api', UserAPI.as_view(), name='api'),
]