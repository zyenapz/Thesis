# Generated by Django 4.1.4 on 2023-01-15 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0002_alter_yearlevel_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
    ]
