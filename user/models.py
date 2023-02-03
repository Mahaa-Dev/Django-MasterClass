from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    no_of_year = models.IntegerField(default=1)

    def __str__(self):
        return self.title
# Create your models here.
