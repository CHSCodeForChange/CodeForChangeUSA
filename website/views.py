from django.shortcuts import render

def club(request):
	return render(request, 'club.html')


def projects(request):
	return render(request, 'projects.html')


def gettingstarted(request):
	return render(request, 'gettingstarted.html')


def contact(request):
	return render(request, 'contact.html')


def home(request):
	return render(request, 'home.html')
