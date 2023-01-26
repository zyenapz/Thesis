# Generated by Django 4.1.4 on 2023-01-26 02:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('visualizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=100, validators=[django.core.validators.MinLengthValidator(10)])),
                ('actual_sentiment', models.CharField(choices=[('POSITIVE', 'Positive'), ('NEUTRAL', 'Neutral'), ('NEGATIVE', 'Negative')], default='NEUTRAL', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluatee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualizer.facultyevaluation')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualizer.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualizer.facultyevaluation')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualizer.section')),
                ('strand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualizer.strand')),
                ('year_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualizer.yearlevel')),
            ],
        ),
        migrations.CreateModel(
            name='SentimentScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vader_pos', models.DecimalField(decimal_places=2, max_digits=4)),
                ('vader_neg', models.DecimalField(decimal_places=2, max_digits=4)),
                ('bert_pos', models.DecimalField(decimal_places=2, max_digits=4)),
                ('bert_neg', models.DecimalField(decimal_places=2, max_digits=4)),
                ('hybrid_pos', models.DecimalField(decimal_places=2, max_digits=4)),
                ('hybrid_neg', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.comment')),
                ('evaluatee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.evaluatee')),
                ('evaluator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.evaluator')),
            ],
        ),
    ]
