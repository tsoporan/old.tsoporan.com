from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
   
    class Meta:
        verbose_name_plural = "Categories"
 
    def __unicode__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=250, unique=True)
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name

class Project(models.Model):
    WEIGHT = tuple(enumerate(range(10)))

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(blank=True)
    url = models.URLField(verify_exists=False) #don't error if website doesn't exist anymore
    created = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client)
    skills = models.ManyToManyField(Skill)
    category = models.ForeignKey(Category)
    description = models.TextField()
    ordering = models.IntegerField(default=1, choices=WEIGHT, help_text="Ordering by least to greatest, i.e 1 is lighter than 5.")

    class Meta:
        ordering = ['ordering']

    @models.permalink
    def get_absolute_url(self):
        return ('portfolio.views.project_detail', (), {'slug': self.slug,})

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Project, self).save()
    
    def __unicode__(self):
        return self.name

class ProjectResource(models.Model):
    name = models.CharField(max_length=255)
    resource = models.FileField(upload_to = "uploads/%Y/%m/%d")
    project = models.ForeignKey(Project, related_name="resources")

    def __unicode__(self):
        return self.resource.name
    



