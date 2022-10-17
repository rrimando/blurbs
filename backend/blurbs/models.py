from django.db import models
from django.conf import settings


class Blurb(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    blurb = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blurb
