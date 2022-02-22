from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from taggit.managers import TaggableManager
from django import forms

# Create your models here.
class Publication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='publication',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    summary = models.TextField(null=True,blank=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, blank=True, unique_for_date=True)
    url = models.URLField()
    created = models.DateField(auto_now_add=True,db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='publication_liked',blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('fanfics:publication_details',args=[self.created.year,self.created.strftime('%m'),self.created.strftime('%d'),self.slug])

class Comment(models.Model):
    publication = models.ForeignKey(Publication,related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='comment',on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True,db_index=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Komentarz dodany przez {self.user.username} dla posta {self.post}'


