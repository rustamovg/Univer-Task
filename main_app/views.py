from django.shortcuts import render
from .forms import UserForm, QuestionForm

def home_page(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        question_form = QuestionForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            return render(request, "success.html")

        if question_form.is_valid():
            question_form.save()
            return render(request, "success.html")

        print(user_form.errors)  # Print form errors if validation fails
        print(question_form.errors)

    else:
        user_form = UserForm()
        question_form = QuestionForm()

    return render(request, "index.html", {"user_form": user_form, "question_form": question_form})
