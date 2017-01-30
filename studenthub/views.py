from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from studenthub.forms import PostForm
from django.core.mail import send_mail
import json

def index(request):
	return render(request, 'studenthub/index.html')

def culturalclubs(request):
	return render(request, 'studenthub/cultural.html')

def technicalclubs(request):
	return render(request, 'studenthub/technical.html')

def sports(request):
	return render(request, 'studenthub/sports.html')

def events(request):
	return render(request, 'studenthub/events.html')
	
def activities(request):
	return render(request, 'studenthub/activities.html')

def edusoc(request):
	return render(request, 'studenthub/edusoc.html')

def contact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		msg = request.POST.get('message')
		sub = "Contact"
		message = msg + "\n" + "\n" + "Phone - " + phone
		send_mail(sub,message,email, ['harshavamsi096@gmail.com'] )
		response_data = {}
		response_data['result'] = "Thanks for contacting us. We'll get back to you soon!"
		return HttpResponse(json.dumps(response_data),content_type="application/json")	
	else:
		return render(request, 'studenthub/index.html')	 

def register(request):
	return HttpResponseRedirect(reverse('studenthub:index'))





