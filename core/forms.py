from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Answer


# User Registration Form
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = None


# Question Form
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "body"]


# Answer Form
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["body"]
