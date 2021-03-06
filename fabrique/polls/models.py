from django.db import models

QUESTION_TYPE = (
    ('0', 'Text'),
    ('1', 'Only one'),
    ('2', 'More than one'),
)


class User(models.Model):
    id = models.IntegerField(primary_key=True, default="0")

    def __str__(self):
        return str(self.id)


class Poll(models.Model):
    title = models.CharField(max_length=200)
    poll_start = models.DateField(auto_now_add=True, editable=False)
    poll_end = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name='questions')
    type = models.CharField(max_length=1, choices=QUESTION_TYPE, default=0)
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=200)

    def __str__(self):
        return 'Question:{} answer: {}'.format(self.question, self.answer)
