from django.shortcuts import render
from .models import Skill


from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["skill_list"] = Skill.objects.all()
        return context
