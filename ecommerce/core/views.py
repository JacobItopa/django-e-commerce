from django.shortcuts import render
from django.views import generic
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

class HomeView(generic.TemplateView):
    template_name = 'index.html'


class ContactView(generic.FormView):
    form_class = ContactForm
    success_url = 'contact'
    template_name = 'contact.html'

    def form_valid(self, form):
        messages.info(self.request, 'Thanks for contacting us')
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message = f"""
        Received message below from {name} {email}

        ________________________


        {message}
        """

        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)

    