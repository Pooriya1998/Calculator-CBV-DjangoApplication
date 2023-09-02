from django.urls import path
from . import views


app_name = 'calculator'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index_view"),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
]