from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroForm
from rest_framework.views import APIView
import json
from apps.usuario.serializers import UserSerializer

class RegistroUsuario (CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy ('mascota:mascota_listar')




class UserAPI (APIView):
	serializer = UserSerializer

	def get(self, request, format=None):
		lista = User.objects.all()
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type = 'application/json')
