from django.shortcuts import render
from .models import SearchQuery 
from arguments.models import ArgumentPost

# Create your views here.
def search_view(request):
	query = request.GET.get('q', None)
	user = None 
	if request.user.is_authenticated:
		user = request.user
	context = {"query":query}
	if query is not None:
		SearchQuery.objects.create(user=user, query=query)
		arguments = ArgumentPost.objects.search(query=query)
		context['arguments']= arguments
	return render(request, 'searches/result.html', context)