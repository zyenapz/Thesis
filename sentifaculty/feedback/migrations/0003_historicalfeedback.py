# Generated by Django 4.1.4 on 2023-01-17 04:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0001_initial'),
        ('users', '0001_initial'),
        ('feedback', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=100, validators=[django.core.validators.MinLengthValidator(10)])),
                ('actual_sentiment', models.CharField(choices=[('POSITIVE', 'POSITIVE'), ('NEUTRAL', 'NEUTRAL'), ('NEGATIVE', 'NEGATIVE')], default='NEUTRAL', max_length=10)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('faculty_eval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualizer.facultyevaluation')),
                ('sentiment_score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.sentimentscore')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacher')),
            ],
        ),
    ]