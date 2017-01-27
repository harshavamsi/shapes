from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from studenthub.forms import PostForm


def index(request):
	return render(request, 'studenthub/index.html')

def register(request):
	return HttpResponseRedirect(reverse('studenthub:index'))





