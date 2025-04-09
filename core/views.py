from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, QuestionForm, AnswerForm
from .models import Question, Answer


def register_view(request):
    """
    Handles user registration.
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Hash password
            user.save()
            login(request, user)
            return redirect("question_list")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    """ "
    Handles user login."
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("question_list")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def question_list_view(request):
    """ "
    Displays a list of questions with the most recent ones first."
    """
    questions = Question.objects.all().order_by("-created_at")
    return render(request, "question_list.html", {"questions": questions})


@login_required
def post_question_view(request):
    """ "
    Handles posting a new question by a logged-in user."
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect("question_list")
    else:
        form = QuestionForm()
    return render(request, "post_question.html", {"form": form})


@login_required
def question_detail_view(request, question_id):
    """ "
    Displays the details of a question, including answers and a form to post a new answer."
    """
    question = get_object_or_404(Question, id=question_id)
    answers = question.answers.all()
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect("question_detail", question_id=question_id)
    else:
        form = AnswerForm()
    return render(request, "question_detail.html", {"question": question, "answers": answers, "form": form})


@login_required
def like_answer_view(request, answer_id):
    """ "
    Handles liking or unliking an answer by a logged-in user.
    """
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
    return redirect("question_detail", question_id=answer.question.id)
