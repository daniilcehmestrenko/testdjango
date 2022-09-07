from django.shortcuts import render
from .models import ContactLink,About
from .forms import ContactForm
from django.views.generic import CreateView
from django.views import View


class ContactView(View):
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm
        return render(request, 'contact/contact.html', {'contacts': contacts, 'form': form})


class CreateContact(CreateView):
    form_class = ContactForm
    success_url = '/'


class AboutView(View):
    def get(self, request):
        about = About.objects.last()
        return render(request, 'contact/about.html', {'contacts': about})

