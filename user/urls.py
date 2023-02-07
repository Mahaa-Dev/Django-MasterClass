from django.urls import path
from .views import IndexPageView, ContactCreate


urlpatterns = [
    path("detail/", IndexPageView.as_view(), name="index"),
    path("contact/", ContactCreate.as_view(), name="contact")
    #path("infoo/", Information.as_view(), name="show_info")

]
