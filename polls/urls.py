# here i am going to write url configration
from . import views
from django.urls import path

urlpatterns = [
    #/polls/
    path('', views.index,name="index"),
    # /polls/10/
    path('<int:question_id>/', views.detail,name='detail'),
    # /polls/10/result
    path('<int:question_id>/results/', views.results,name='results'),
    # /polls/10/vote/
    path('<int:question_id>/vote/', views.vote_tally,name='vote_tally')
]
