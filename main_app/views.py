from django.shortcuts import render
from .forms import UserForm, QuestionForm

def home_page(request):
    message = None
    if request.method == "POST":
        user_form = UserForm(request.POST)
        question_form = QuestionForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            message = "The registration request has been successfully sent"

        elif question_form.is_valid():
            question_form.save()
            message = "The question has been successfully sent"
        else:
            message = "There were errors in your form submission. Please check your inputs"

        print(user_form.errors)
        print(question_form.errors)

    else:
        user_form = UserForm()
        question_form = QuestionForm()

    return render(request, "index.html", 
                  {"user_form": user_form,
                   "question_form": question_form,
                   "message": message})
