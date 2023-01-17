# Generated by Django 4.1.4 on 2023-01-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_historicalfeedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='actual_sentiment',
            field=models.CharField(choices=[('POSITIVE', 'Positive'), ('NEUTRAL', 'Neutral'), ('NEGATIVE', 'Negative')], default='NEUTRAL', max_length=10),
        ),
        migrations.AlterField(
            model_name='historicalfeedback',
            name='actual_sentiment',
            field=models.CharField(choices=[('POSITIVE', 'Positive'), ('NEUTRAL', 'Neutral'), ('NEGATIVE', 'Negative')], default='NEUTRAL', max_length=10),
        ),
    ]
