# Generated by Django 4.1.4 on 2023-01-15 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yearlevel',
            name='level',
            field=models.CharField(choices=[('Grade 11', 'Grade 11'), ('Grade 12', 'Grade 12')], max_length=10, unique=True),
        ),
    ]