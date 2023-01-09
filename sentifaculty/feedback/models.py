from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import Student, Teacher 
from visualizer.models import AcademicYear


class SentimentScore(models.Model):
    MAX_DIGITS = 4
    MAX_DECIMAL = 2

    vader_pos = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=MAX_DECIMAL)
    vader_neg = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=MAX_DECIMAL)
    bert_pos = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=MAX_DECIMAL)
    bert_neg = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=MAX_DECIMAL)
    hybrid_pos = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=MAX_DECIMAL)
    hybrid_neg = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=MAX_DECIMAL)

class Feedback(models.Model):
    class SentimentChoice(models.TextChoices):
        POSITIVE = "POSITIVE", _('POSITIVE')
        NEUTRAL = "NEUTRAL", _('NEUTRAL')
        NEGATIVE = "NEGATIVE", _('NEGATIVE')

    comment = models.TextField(max_length=100, validators=[
                               validators.MinLengthValidator(10)])
    actual_sentiment = models.CharField(
        max_length=10, choices=SentimentChoice.choices, default=SentimentChoice.NEUTRAL)
    submission_date = models.DateTimeField(auto_now_add=True)

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    sentiment_score = models.ForeignKey(SentimentScore, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.comment