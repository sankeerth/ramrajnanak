from django.shortcuts import render
from django.core.mail import EmailMessage	

from .forms import ContactForm

# Create your views here.

def home(request):
	return render(request, "home.html", {})

def about(request):
	return render(request, "about.html", {})

def contact(request):
	title = 'Contact Me'
	form = ContactForm(request.POST or None)

	if form.is_valid():
		email = EmailMessage('Hello', 'World', to=['sankeerth456@gmail.com'])
		email.send()

	context = {
		'title': title,
		'form': form,
	}
	return render(request, "contact.html", context)

def gallery(request):
	return render(request, "gallery.html", {})