from django.urls import path
from .views import IndexPageView, Information


urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("infoo/", Information.as_view(), name="show_info")

]
