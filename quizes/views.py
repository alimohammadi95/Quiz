from django.http import HttpResponse
from django.shortcuts import render
from quizes.models import Quiz


def quiz(request):
    if request.method == "GET":
        question = Quiz.objects.all("question")
        user = None
        context = {
            "question": question,
            "user": user,
        }
        render(request, "base.html", context=context)
    elif request.method == "POST":
        return HttpResponse("here is the result")

