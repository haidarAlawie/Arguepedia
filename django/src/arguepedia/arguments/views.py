from django.contrib.auth.decorators import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from .models import ArgumentPost
from .forms import ArgumentPostModelForm


def argument_post_list_view(request):
	#all the arguments
	qs = ArgumentPost.objects.all()
	template_name = 'arguments/argument_post_list.html'
	context = {'arguments_list':qs}
	return render(request,template_name,context)

@login_required
def argument_post_create_view(request):

	form = ArgumentPostModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		form.save()
		obj = ArgumentPostModelForm()
		form = ArgumentPostModelForm()

	template_name = 'arguments/form.html'
	context = {'form': form}
	return render(request,template_name,context)


def argument_post_detail_view(request, post_id): 
	template_name = 'arguments/argument_post_detail.html'
	obj = get_object_or_404(ArgumentPost, id=post_id) 
	context = {"argument": obj}
	return render(request,template_name,context)


def argument_post_update_view(request, post_id):
	obj = get_object_or_404(ArgumentPost, id=post_id) 
	form = ArgumentPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name = 'arguments/form.html'
	context = {'form':form, "title":f"Update {obj.title}"}
	return render(request,template_name,context)


def argument_post_delete_view(request, post_id):
	template_name = 'arguments/argument_post_delete.html'
	obj = get_object_or_404(ArgumentPost, id=post_id) 
	
	if request.method =="POST":
		obj.delete()
		return redirect("/arguments/")

	context = {"object": obj}
	return render(request,template_name,context)
