from django.contrib import admin
from portfolio.models import Client, Skill, Project, ProjectResource

class ResourceInline(admin.StackedInline):
    model = ProjectResource
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ResourceInline]

admin.site.register(Client)
admin.site.register(Skill)
admin.site.register(Project, ProjectAdmin)
    
