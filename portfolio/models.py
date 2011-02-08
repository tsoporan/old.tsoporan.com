from django.db import models
from django.template.defaultfilters import slugify

class Client(models.Model):
    name = models.CharField(max_length=250, unique=True)
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client)
    skills = models.ManyToManyField(Skill)

    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.project_detail', (), {'slug': self.slug,})

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.name


class ProjectResource(models.Model):
    resource = models.FileField(upload_to = "uploads/%Y/%m%/d")
    description = models.TextField()    
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.resource.name
    



