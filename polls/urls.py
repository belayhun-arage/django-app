# here i am going to write url configration
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('about', views.about),
    path('q',views.questionList)
]
