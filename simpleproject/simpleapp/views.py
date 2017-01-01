from django.shortcuts import render
from .forms import RegisterForm
from .models import UserModel
from django.http import HttpResponse
# Create your views here.
def hello(request):
	form = RegisterForm()
	return render(request, "hello.html", {"form" : form})

def saveUser(request):

	resp = ''

	if request.POST:
		form = RegisterForm(data = request.POST)

		if form.is_valid():
			newUser = UserModel(
				firstName 	= request.POST.get('firstName',''),
				lastName 	= request.POST.get('lastName',''),
				email 		= request.POST.get('email',''),
				password 	= request.POST.get('password','')
			)

			newUser.save()
			resp = 'Saved Successfully'
		else:
			resp = 'Form invalid'
	else:
		resp = 'Invalid request'

	return HttpResponse(resp)
