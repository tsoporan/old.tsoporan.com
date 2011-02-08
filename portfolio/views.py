from django.shortcuts import render_to_response
from django.template import RequestContext

from portfolio.models import Project

def index(request, template="portfolio/index.html"):
    return render_to_response(template, {}, context_instance=RequestContext(request))
