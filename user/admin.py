from django.contrib import admin

from .models import Skill, MyDetail,Contact

admin.site.register([
    Skill,
    MyDetail,
    Contact
])

# Register your models here.
