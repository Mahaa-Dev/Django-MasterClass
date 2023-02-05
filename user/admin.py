from django.contrib import admin

from .models import Skill, MyDetail

admin.site.register([
    Skill,
    MyDetail
])

# Register your models here.
