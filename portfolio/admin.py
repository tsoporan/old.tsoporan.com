from django.contrib import admin
from portfolio.models import Category, Client, Skill, Project, ProjectResource

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ResourceInline(admin.StackedInline):
    model = ProjectResource
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ResourceInline]
    list_display = ('name', 'ordering', 'url', 'created', 'description')

admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
    
