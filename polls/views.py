from django.shortcuts import render


from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    output = ", ".join(q.question_text for q in latest_questions)
    return HttpResponse(output)

def test(request):
    return HttpResponse("Test link")

def detail(request, question_id):
    return HttpResponse("You are looking at details for question #%s" % question_id)

def results(request, question_id):
    return HttpResponse("You are looking at results for question #%s" % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting for question #%s" % question_id)

