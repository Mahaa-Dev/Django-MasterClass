from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    no_of_year = models.IntegerField(default=1)

    def __str__(self):
        return self.title
# Create your models here.

class MyDetail(models.Model):
    name = models.CharField(max_length=255)
    education_details = models.TextField(null=True, blank=True)
    technical_skill = models.CharField(max_length=255)
    working_experience = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}{self.education_details}{self.technical_skill}{self.working_experience}"
