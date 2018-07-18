from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
	'''log the user out.'''
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
	'''register a new user here.'''
	if request.method != "POST":
		#display blank registration form.
		form = UserCreationForm()
		
	else:
		#process completed form.
		form = UserCreationForm(data=request.POST)
		
		if form.is_valid():
			# the submitted data is valid, we call the form’s save() method to save username and password.
			new_user = form.save()
			
			#after saving the info. log the user in and redirect to the home page.
			#Here we get the value associated with the 'password1' key in the form’s POST data.
			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))
			
	context = {'form':form}
	
	return render(request, 'users/register.html', context)
