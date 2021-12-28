from django.http import HttpResponse
from .models import Question

def index(request):
    return HttpResponse("Hello,Wellcome to the home page.")

# define a view for seeing the details of a particalr # QUESTION:
def detail(request,question_id):
    return HttpResponse("You are visiting the question %s."%question_id)

# define a view for seeing the results of a particular # QUESTION:
def results(request,question_id):
    response="You are looking for the results of question %s"
    return HttpResponse(response %question_id)

# define a view in order to vote for a particlar # QUESTION:
def vote_tally(request,question_id):
    return HttpResponse("voting")
