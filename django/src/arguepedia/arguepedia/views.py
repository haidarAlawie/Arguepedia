from django.http import HttpResponse
from django.shortcuts import render
from arguments.models import ArgumentPost


def index_page(request):
	qs= ArgumentPost.objects.all()[:5]
	
	template_name = 'arguepedia/index.html'
	context = {"title": "Home", "argument_list": qs}
	return render(request, template_name, context)

def contactus_page(request):
	print(request.POST)
	template_name = 'arguepedia/form.html'
	context = {"title": "Contact us"}
	return render(request, template_name, context)

 