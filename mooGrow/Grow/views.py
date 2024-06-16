from django.shortcuts import render
from django.contrib import messages
from django.db.models.query_utils import Q
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest
from Grow.models import join,put,cart

# Create your views here.

def index(request):

    return render(request, 'index.html', {})

def msg(request):
	if request.method == 'POST':
		full = request.POST['name']
		number = request.POST['phone']
		comment = request.POST['ms']

		saverecord=join()
		saverecord.Fullname=full
		saverecord.Mobileno=number
		saverecord.Message=comment
		saverecord.save()
		view="Contact message send successfuly"
		return render(request, 'index.html', {'con':view})

def login(request):
	if request.method == 'POST':
		full = request.POST['name']
		e = request.POST['mail']
		pany = request.POST['company']
		site = request.POST['web']
		number = request.POST['phone']
		comment = request.POST['msg']

		saverecord=put()
		saverecord.Fullname=full
		saverecord.Email=e
		saverecord.Company=pany
		saverecord.Website=site
		saverecord.Mobileno=number
		saverecord.Message=comment
		saverecord.save()
		view="login successfuly"
		return render(request, 'index.html', {'log':view})

def order(request):
	if request.method == 'POST':
		full = request.POST['name']
		number = request.POST['phone']
		e = request.POST['mail']
		pany = request.POST['company']
		comment = request.POST['msg']

		saverecord=cart()
		saverecord.Fullname=full
		saverecord.Mobileno=number
		saverecord.Email=e
		saverecord.Company=pany        
		saverecord.Message=comment
		saverecord.save()
		view="order successfuly"
		return render(request, 'index.html', {'der':view})
