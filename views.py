from django.shortcuts import render
from .models import Submission


def submit(request, course_id):

    if request.method == "POST":
        return render(request, "result.html")

    return render(request, "submit.html")


def show_exam_result(request, course_id, submission_id):

    context = {
        "score": 3
    }

    return render(request, "result.html", context)
