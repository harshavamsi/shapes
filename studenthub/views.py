from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from studenthub.forms import PostForm
from django.core.mail import send_mail
from .models import *
import json

def index(request):
	return render(request, 'studenthub/index.html')

def culturalclubs(request):
	d=dance.objects.get(pk=1)
	m=music.objects.get(pk=1)
	#s=sankalp.objects.get(pk=1)
	t=theatre.objects.get(pk=1)
	q=quiz.objects.get(pk=1)
	context={'music':m,'quiz':q,'theatre':t, 'dance' : d}
	return render(request, 'studenthub/cultural.html',context)

def technicalclubs(request):
	a=acm.objects.get(pk=1)
	i=ieee.objects.get(pk=1)
	#e = enigma.objects.get(pk=1)
	#aa = avions.objects.get(pk=1)
	context={'acm':a,'ieee':i,}
	return render(request, 'studenthub/technical.html',context)

def sports(request):
	return render(request, 'studenthub/sports.html')

def events(request):
	return render(request, 'studenthub/events.html')

def contact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		msg = request.POST.get('message')
		c = Contact(name = name, email = email , phone = phone, message = msg)
		c.save()
		sub = "Contact"
		message = msg + "\n" + "\n" + "Phone - " + phone
		send_mail(sub,message,email, ['harshavamsi096@gmail.com'] )
		response_data = {}
		response_data['result'] = "Thanks for contacting us. We'll get back to you soon!"
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return render(request, 'studenthub/index.html')


def dancecontact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		msg = request.POST.get('message')
		sub = "Contact"
		c = danceContact(name = name, email = email , phone = phone, message = msg)
		c.save()
		message = msg + "\n" + "\n" + "Phone - " + phone
		send_mail(sub,message,email, ['harshavamsi096@gmail.com'] )
		response_data = {}
		response_data['result'] = "Thanks for contacting us. We'll get back to you soon!"
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return render(request, 'studenthub/index.html')



def musiccontact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		msg = request.POST.get('message')
		sub = "Contact"
		c = musicContact(name = name, email = email , phone = phone, message = msg)
		c.save()
		message = msg + "\n" + "\n" + "Phone - " + phone
		send_mail(sub,message,email, ['harshavamsi096@gmail.com'] )
		response_data = {}
		response_data['result'] = "Thanks for contacting us. We'll get back to you soon!"
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return render(request, 'studenthub/index.html')


def quizcontact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		msg = request.POST.get('message')
		sub = "Contact"
		c = quizContact(name = name, email = email , phone = phone, message = msg)
		c.save()
		message = msg + "\n" + "\n" + "Phone - " + phone
		send_mail(sub,message,email, ['harshavamsi096@gmail.com'] )
		response_data = {}
		response_data['result'] = "Thanks for contacting us. We'll get back to you soon!"
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return render(request, 'studenthub/index.html')


def theatrecontact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		msg = request.POST.get('message')
		sub = "Contact"
		c = theatreContact(name = name, email = email , phone = phone, message = msg)
		c.save()
		message = msg + "\n" + "\n" + "Phone - " + phone
		send_mail(sub,message,email, ['harshavamsi096@gmail.com'] )
		response_data = {}
		response_data['result'] = "Thanks for contacting us. We'll get back to you soon!"
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return render(request, 'studenthub/index.html')




def acmcontact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		msg = request.POST.get('message')
		sub = "Contact"
		c = acmContact(name = name, email = email , phone = phone, message = msg)
		c.save()
		message = msg + "\n" + "\n" + "Phone - " + phone
		send_mail(sub,message,email, ['harshavamsi096@gmail.com'] )
		response_data = {}
		response_data['result'] = "Thanks for contacting us. We'll get back to you soon!"
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return render(request, 'studenthub/index.html')




def ieeecontact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		msg = request.POST.get('message')
		sub = "Contact"
		c = ieeeContact(name = name, email = email , phone = phone, message = msg)
		c.save()
		message = msg + "\n" + "\n" + "Phone - " + phone
		send_mail(sub,message,email, ['harshavamsi096@gmail.com'] )
		response_data = {}
		response_data['result'] = "Thanks for contacting us. We'll get back to you soon!"
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return render(request, 'studenthub/index.html')


def avionscontact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		msg = request.POST.get('message')
		sub = "Contact"
		c = avionsContact(name = name, email = email , phone = phone, message = msg)
		c.save()
		message = msg + "\n" + "\n" + "Phone - " + phone
		send_mail(sub,message,email, ['harshavamsi096@gmail.com'] )
		response_data = {}
		response_data['result'] = "Thanks for contacting us. We'll get back to you soon!"
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return render(request, 'studenthub/index.html')

def enigmacontact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		msg = request.POST.get('message')
		sub = "Contact"
		c = enigmaContact(name = name, email = email , phone = phone, message = msg)
		c.save()
		message = msg + "\n" + "\n" + "Phone - " + phone
		send_mail(sub,message,email, ['harshavamsi096@gmail.com'] )
		response_data = {}
		response_data['result'] = "Thanks for contacting us. We'll get back to you soon!"
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return render(request, 'studenthub/index.html')



def sankalpcontact(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		msg = request.POST.get('message')
		sub = "Contact"
		c = sankalpContact(name = name, email = email , phone = phone, message = msg)
		c.save()
		message = msg + "\n" + "\n" + "Phone - " + phone
		send_mail(sub,message,email, ['harshavamsi096@gmail.com'] )
		response_data = {}
		response_data['result'] = "Thanks for contacting us. We'll get back to you soon!"
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		return render(request, 'studenthub/index.html')