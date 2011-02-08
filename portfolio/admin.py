from django.contrib import admin
from portfolio.models import Client, Skill, Project, ProjectResource

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ResourceInline(admin.StackedInline):
    model = ProjectResource
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ResourceInline]
    list_display = ('name', 'slug', 'url', 'created', 'description')

admin.site.register(Client)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
    
