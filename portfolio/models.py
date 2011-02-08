from django.db import models
from django.template.defaultfilters import slugify

class Project(models.Model):
    name = models.CharField(max_length=250, help_text="Name of the project.", unique=True)
    slug = models.SlugField(blank=True)

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.name

    



