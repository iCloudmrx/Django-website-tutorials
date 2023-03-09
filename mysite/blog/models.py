from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    title = models.CharField("Article title", max_length=200)
    subtitle = models.CharField(
        "Article subtitle", max_length=200, default="", blank=True)
    article_slug = models.SlugField("Article slug", max_length=255,
                                    null=False, blank=False, unique=True)
    content = models.TextField("Article content")
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.article_slug


class Series(models.Model):
    title = models.CharField("Series title", max_length=200)
    subtitle = models.CharField(
        "Series subtitle", max_length=200, default="", blank=True)
    article_slug = models.SlugField("Series slug", max_length=255,
                                    null=False, blank=False, unique=True)
    published = models.DateTimeField("Date published", default=timezone.now)

    def __str__(self):
        return self.title
