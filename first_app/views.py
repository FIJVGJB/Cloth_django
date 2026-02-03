from django.shortcuts import render


def home(request):
	return render(request, 'first_app/home.html')


def collections(request):
	return render(request, 'first_app/collections.html')


def about(request):
	return render(request, 'first_app/about.html')


def contact(request):
	return render(request, 'first_app/contact.html')

