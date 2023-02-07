from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    no_of_year = models.IntegerField(default=1)

    def __str__(self):
        return self.title
# Create your models here.


class MyDetail(models.Model):
    full_name = models.CharField(max_length=255)
    professional_title = models.CharField(
        max_length=255, null=True, blank=True)
    current_company_name = models.CharField(
        max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="detail/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    resume = models.FileField(
        upload_to="detail/cv/", null=True, blank=True, verbose_name="Updated Resume")

    def __str__(self):
        return self.full_name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"


# class Skill(models.Model):
#     name = models.CharField(max_length=100)
#     level = models.PositiveSmallIntegerField()

#     def __str__(self):
#         return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_replied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"
