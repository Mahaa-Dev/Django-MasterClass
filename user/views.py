from django.shortcuts import render
from .models import Skill, MyDetail


from django.views.generic import TemplateView


# class IndexPageView(TemplateView):
#     template_name = "index.html"

#     def get_context_data(self, *args, **kwargs):
#         # context = super().get_context_data(*args, **kwargs)
#         # context["skill_list"] = Skill.objects.all()
#         context_1 = super().get_context_data(*args, **kwargs)
#         context_1["details"] = MyDetail.objects.all()
#         return context_1

class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["skill_list"] = Skill.objects.all()
        context_1 = {"details": MyDetail.objects.all()}
        context.update(context_1)
        return context


class Information(TemplateView):
    template_name = "info.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["details"] = MyDetail.objects.all()

        return context
