from django.urls import path
from .views import *

urlpatterns = [
    path("", question_list_view, name="question_list"),  # Home page
    path("register/", register_view, name="register"),  # User registration
    path("login/", login_view, name="login"),  # User login
    path("logout/", logout_view, name="logout"),  # User logout
    path("post-question/", post_question_view, name="post_question"),  # Post a new question
    path("question/<int:question_id>/", question_detail_view, name="question_detail"),  # View question details
    path("like-answer/<int:answer_id>/", like_answer_view, name="like_answer"),  # Like an answer
]
