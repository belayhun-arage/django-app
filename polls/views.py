from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_questions= Question.objects.order_by('-pub_date')[:5]
    print(latest_questions)
    # output=','.join([q.question_text for q in latest_questions])
    template=loader.get_template('polls/index.html')
    context={
        'latest_questions':latest_questions
    }
    return HttpResponse(template.render(context,request))

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
