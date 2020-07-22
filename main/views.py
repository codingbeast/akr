from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.

class homepage(View):
	def get(self, request):
		return HttpResponse("COMING SOON")