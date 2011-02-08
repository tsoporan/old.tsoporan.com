from django.shortcuts import render_to_response
from django.template import RequestContext
from portfolio.models import Project
from portfolio.forms import ContactForm
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list, object_detail

def index(request, template="portfolio/index.html"):
    context = {
        'projects': Project.objects.all(),
    }
    return direct_to_template(request, template, extra_context=context)

def about(request, template='portfolio/about.html'):
    return direct_to_template(request, template)

def work(request, template='portfolio/work.html'):
    pass

def contact(request, template='portfolio/contact.html'):
    pass
