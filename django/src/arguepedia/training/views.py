from django.shortcuts import render

# Create your views here.
def testing_view(request):
	template_name = "testing.html"
	context= {}
	return render(request, template_name, context )