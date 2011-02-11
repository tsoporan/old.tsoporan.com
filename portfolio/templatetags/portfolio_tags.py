from django import template
from portfolio.models import ProjectResource
import re

register = template.Library()

def do_get_resource(parser, token):
    try:
        tag_name, project, name, _as, var = token.contents.split()
    except ValueError:
        raise template.TemplateSyntaxError("% tag requires arguments." % token.contents.split()[0])

    if not (name[0] == name[-1] and name[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%s tag's argument should be in quotes." % tag_name)

    return GetResourceNode(project, name[1:-1], var)

class GetResourceNode(template.Node):
    def __init__(self, project, name, var_name):
        self.project = template.Variable(project)
        self.name = name
        self.var_name = var_name

    def render(self, context):
        actual_project = self.project.resolve(context)
        try:
            context[self.var_name] =  ProjectResource.objects.get(project=actual_project, name__iexact=self.name)
        except ProjectResource.DoesNotExist:
            pass
        return ''       
 
register.tag('get_resource', do_get_resource)
