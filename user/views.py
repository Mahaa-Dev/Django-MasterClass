from django.shortcuts import render
from .models import Skill, MyDetail, Contact
from .forms import ContactForm


from django.views.generic import TemplateView, CreateView


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
        context["details"] = MyDetail.objects.last()
        context["form"] = ContactForm()

        return context


# class Information(TemplateView):
#     template_name = "info.html"

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)


#         return context

class ContactCreate(CreateView):
    template_name = "contact_create.html"
    model = Contact
    form_class = ContactForm
    success_url = "/user/detail/"
