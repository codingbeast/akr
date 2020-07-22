from django.shortcuts import render, HttpResponse
from django.views import View
import time
import requests
import json
# Create your views here.
# https://completion.amazon.com/api/2017/suggestions?lop=en_US&mid=ATVPDKIKX0DER&alias=aps&prefix=a
class keyword_cloud(View):
	def get(self, request):
		return render(request,"amazon/index.html")
	def post(self, request):
		keyword = request.POST.get('keyword', '')
		if len(keyword)<1:
			data = ""
			time.sleep(10)
			return render(request,"amazon/index.html",context={"data" : data})
		obj = Scraper()

		data = obj.keyword_finder(keyword=keyword)
		return render(request,"amazon/index.html",context={"data" : data})

class Scraper:
	def keyword_finder(self,keyword):
		container = []
		
		base = "https://completion.amazon.com/api/2017/suggestions?lop=en_US&mid=ATVPDKIKX0DER&alias=aps&prefix={}".format(keyword)
		response = requests.get(base).json()
		suggestions=response['suggestions']
		suggestions_keywords = [i['value'] for i in suggestions]
		temp = {
			"key" : keyword,
			"value" : suggestions_keywords
		}
		container.append(temp)
		abcd ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		for alfa in abcd:
			keyword_ = "{} {}".format(keyword,alfa)
			base_ = "https://completion.amazon.com/api/2017/suggestions?lop=en_US&mid=ATVPDKIKX0DER&alias=aps&prefix={}".format(keyword_)
			response = requests.get(base_).json()
			suggestions=response['suggestions']
			suggestions_keywords = [i['value'] for i in suggestions]
			temp = {
				"key" : keyword_,
				"value" : suggestions_keywords
			}
			container.append(temp)
		return container

