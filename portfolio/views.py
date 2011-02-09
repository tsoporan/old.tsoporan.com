from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from portfolio.models import Project
from portfolio.forms import AkismetContactForm
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list, object_detail
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request, template="portfolio/index.html"):
    if request.method == 'POST' and request.POST:
        form = AkismetContactForm(meta=request.META, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            from_email = settings.DEFAULT_FROM_EMAIL
            to_emails = [m[1] for m in settings.MANAGERS] 
            
            message_subject = "Contacted on {}".format(Site.objects.get_current().domain)
            message_template =  """Who: {}\n\nE-mail: {}\n\nMessage: {}\n\n""".format(cd['name'], cd['email'], cd['message'])

            #send mail
            send_mail(message_subject, message_template, from_email, to_emails, fail_silently=False)
            messages.success(request, "Thanks for sending that email!")
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AkismetContactForm()
    context = {
        'projects': Project.objects.all(),
        'form': form,
    }
    return direct_to_template(request, template, extra_context=context)

def about(request, template='portfolio/about.html'):
    return direct_to_template(request, template)

def work(request, template='portfolio/work.html'):
    return direct_to_template(request, template)

def contact(request, template='portfolio/contact.html'):
    return direct_to_template(request, template)
