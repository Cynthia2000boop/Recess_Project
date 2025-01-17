from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm


def home(request):
	return render(request, 'index.html')


def course(request):
	return render(request, 'course.html')


def facility(request):
	return render(request, 'facility.html')


def instructor(request):
	return render(request, 'instructor.html')



def dashboard(request):
	if request.user.is_authenticated:
		return render(request, 'dashboard/pages/dashboard.html')
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	


def courses(request):
	return render(request, 'dashboard/pages/courses.html')





def facilities(request):
	return render(request, 'dashboard/pages/facilities.html')




def instructors(request):
	return render(request, 'dashboard/pages/instructors.html')



def profile(request):
	if request.user.is_authenticated:
		return render(request, 'dashboard/pages/profile.html')
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('sign_in')
	
	



def signout(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')



def signin(request):
	if request.user.is_authenticated:
		return render(request, 'dashboard/pages/dashboard.html')
	else:
		# Check to see if logging in
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			# Authenticate
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, "You Have Been Logged In!")
				return redirect('dashboard')
			else:
				messages.success(request, "There Was An Error Logging In, Please Try Again...")
				return redirect('home')
		else:
			return render(request, 'dashboard/pages/sign_in.html')
		

	




def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('dashboard')
	else:
		form = SignUpForm()
		return render(request, 'dashboard/pages/sign_up.html', {'form':form})

	return render(request, 'dashboard/pages/sign_up.html', {'form':form})
