# Generated by Django 4.1.4 on 2023-02-10 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strand',
            name='strand_name',
            field=models.CharField(choices=[('STEM', 'STEM'), ('ABM', 'ABM'), ('HUMSS', 'HUMSS'), ('ICT', 'ICT')], default='HUMSS', max_length=10, unique=True),
        ),
    ]
