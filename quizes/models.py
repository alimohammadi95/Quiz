from django.db import models

class Quiz(models.Model):
    question = models.TextField()
    user = models.ManyToManyField(question, related_name="question")
