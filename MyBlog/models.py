from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse

from ckeditor.fields import RichTextField

from django.http import HttpResponseRedirect

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=250, default="wpis")

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200, default=None)
    content = RichTextField(blank=True, null=True)
    # content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    published = models.DateTimeField(
        default=timezone.now, verbose_name="Publication date"
    )
    created = models.DateTimeField(default=timezone.now, verbose_name="Created")

    options = (("draft", "Draft"), ("published", "Published"))

    status = models.CharField(max_length=10, choices=options, default="draft")
    image = models.ImageField(upload_to="images/", default="pic")
    likes = models.ManyToManyField(User, related_name="blog_post")

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse("details", args=[str(self.id)])

