from django.contrib.auth.decorators import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from .models import ArgumentPost
from .forms import ArgumentPostModelForm
from . models import Action
from .forms import ActionForm


def argue_view(request,post_id):
	template_name = 'arguments/argue.html'
	#display the argument that is to be debated
	argument = get_object_or_404(ArgumentPost, id=post_id) 
	action_argument = get_object_or_404(ArgumentPost, id=post_id) 
	#counter argument
	action_form = ActionForm(request.POST or None, request.FILES or None)
	counter_argument_form = ArgumentPostModelForm(request.POST or None, request.FILES or None)
	if counter_argument_form.is_valid():
		obj2 = counter_argument_form.save(commit = False)
		obj2.user = request.user
		obj2.attacking = argument
		obj2.parent = argument
		if argument.root_argument is None:
			obj2.root_argument = argument
		else:
			obj2.root_argument = argument.root_argument


	if action_form.is_valid():
		action_obj = action_form.save(commit = False)

		action_form.save()
		counter_argument_form.save()

	context={
	"argument":argument,
	"action_argument": action_argument,
	"counter_argument_form": counter_argument_form,
	"action_form":action_form

	 }
	return render(request,template_name,context)

def graph_view(request):
	template_name = 'arguments/graph.html'
	context = {}
	return render(request, template_name, context)


def list_view(request):
	#all the arguments
	qs = ArgumentPost.objects.all()
	template_name = 'arguments/list.html'
	context = {'arguments_list':qs}
	return render(request,template_name,context)

@login_required(login_url='/user/login/')
def create_view(request):

	form = ArgumentPostModelForm(request.POST or None, request.FILES or None)
	action_form = ActionForm(request.POST or None, request.FILES or None)
	
		#action form
	if action_form.is_valid():
		obj2 = action_form.save(commit = False)
		innder_id = obj2.id
		
		action_form.save()

		
	#argument form
	if form.is_valid():
		
		obj = form.save(commit=False)
		obj.action = Action.objects.get(id=obj2.id)
		obj.user = request.user
		obj.root_argument = None

		form.save()
		


	template_name = 'arguments/create.html'
	context = {'form': form, 'action_form':action_form}
	return render(request,template_name,context)


def detail_view(request, post_id): 
	template_name = 'arguments/detail.html'
	obj = get_object_or_404(ArgumentPost, id=post_id) 
	context = {"argument": obj}
	return render(request,template_name,context)


def update_view(request, post_id):
	obj = get_object_or_404(ArgumentPost, id=post_id) 
	form = ArgumentPostModelForm(request.POST or None, instance=obj)

	if form.is_valid():
		form.save()
	template_name = 'arguments/form.html'
	context = {'form':form, "title":f"Update {obj.title}"}
	return render(request,template_name,context)


def delete_view(request, post_id):
	template_name = 'arguments/delete.html'
	obj = get_object_or_404(ArgumentPost, id=post_id) 
	if request.method =="POST":
		obj.delete()
		return redirect("/arguments/")

	context = {"object": obj}
	return render(request,template_name,context)
