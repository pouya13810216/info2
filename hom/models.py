from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.utils import timezone
import jdatetime
from django.urls import reverse

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    article = models.ForeignKey('Articel', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.article.title}"
class Live_index(models.Model):
    about=models.TextField( blank=False , null=False)
    img_about = models.ImageField(upload_to='uploads/', null=False, blank=False )


    def __str__(self):
         return self.about

class Articel(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = HTMLField(null=False, blank=False)
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(allow_unicode=True, blank=True)
    img = models.ImageField(upload_to='uploads/aricels', blank=True)
    puplic = models.CharField(default="پویا دلنواز", max_length=100)

    @property
    def date_j(self):
        return jdatetime.datetime.fromgregorian(datetime=self.date).strftime('%Y/%m/%d')

    def save(self, *args, **kwargs):
        if not self.slug:
            raw_slug = slugify(self.title)
            self.slug = raw_slug.replace('-', '')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("singleblog", kwargs={"slug": self.slug})
    
    
class history(models.Model):
        history_title=models.CharField(null=True, max_length=120)
        history_img = models.ImageField(upload_to='uploads/history/', null=True, blank=True, default='default.jpg')

        def __str__(self):
             return self.history_title
        



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"