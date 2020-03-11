from django.http import HttpResponse
from django.shortcuts import render
from arguments.models import ArgumentPost
from plotly.offline import plot
import plotly.graph_objects as go

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

def graph1_page(request):
	print(request.POST)
	template_name = 'arguepedia/graph1.html'
	context = {"title": "Contact us"}
	return render(request, template_name, context)

