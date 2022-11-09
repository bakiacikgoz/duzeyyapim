from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from . forms import ContactForm
from django.urls import reverse_lazy
# Create your views here.

class ContactView(FormView,TemplateView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

