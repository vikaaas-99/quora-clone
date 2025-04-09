from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """ "
    Model representing a question in the Q&A system."
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    """ "
    Model representing an answer to a question in the Q&A system.""
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="liked_answers", blank=True)

    def __str__(self):
        return f"Answer by {self.user.username}"
