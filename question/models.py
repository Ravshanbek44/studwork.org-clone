from django.db import models
from user.models import Account, Subject


class Question(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject_question = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_questions')
    question = models.TextField()
    image = models.ImageField(upload_to='questions/', null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    is_answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.phone

    @property
    def get_count_answers(self):
        return self.question_answers.count()


class Answer(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answers')
    image = models.ImageField(upload_to='answers', null=True, blank=True)
    answer = models.TextField()

    def __str__(self):
        return self.user.phone
