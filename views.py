from django.shortcuts import render
from .models import Event
from django.http import HttpResponseRedirect
from .forms import Event_form
from django.http import JsonResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
import pdfkit



def add_event(request):
    submitted = False
    if request.method == "POST":
        form = Event_form(request.POST)
        if form.is_valid():
            form.save()
            send_email_from_app(form.cleaned_data)
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = Event_form
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})


def home(request):
    return render(request, 'events/home.html', {})


def send_email_api(request):
    send_email_from_app()
    data = {
        'succes':True,
        'message':'api to send e-mail'
    }

    return JsonResponse(data)


def send_email_from_app(data):
    html_tpl_path = 'p1ft3fd0481fom13cbingnu61okq4-html.html'
    email_html_template = get_template(html_tpl_path).render({'data': data, 'base_dir': 'C:/Users/diart/PycharmProjects/fg/events/templates'})

    options = {
        "enable-local-file-access": ""
    }
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    pdfkit.from_string(email_html_template, 'FGEnergy.pdf', configuration=config, options=options)
    receiver_email = data['email']

    email_msg = EmailMessage('FGenergy Presentation Test',
                             '', settings.APPLICATION_EMAIL,
                             [receiver_email],
                             reply_to=[settings.APPLICATION_EMAIL]
                             )
    email_msg.content_subtype = 'text'
    email_msg.attach_file('FGEnergy.pdf')
    email_msg.send(fail_silently=False)
