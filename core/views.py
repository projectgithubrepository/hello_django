from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome):
	return HttpResponse('<h1>Hello {}</h1>'.format(nome))

def soma(request, num1, num2):
	soma = num1 + num2
	return HttpResponse('<h1>soma de {} + {} = {} </h1>'.format(num1, num2, soma))