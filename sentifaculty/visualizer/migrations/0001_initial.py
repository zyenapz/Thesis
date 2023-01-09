# Generated by Django 4.1.4 on 2023-01-09 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('start_year', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('end_year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_ID', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Strand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strand_name', models.CharField(choices=[('ABM', 'ABM'), ('ABM-B', 'ABM-B'), ('ABMBUS', 'ABMBUS'), ('HE', 'HE'), ('HUMS', 'HUMS'), ('HUMSS', 'HUMSS'), ('ICT', 'ICT'), ('STEM', 'STEM'), ('STEM-M', 'STEM-M'), ('STEM-S', 'STEM-S'), ('STEMB', 'STEMB'), ('STEMF', 'STEMF'), ('STEMG', 'STEMG'), ('STEMMA', 'STEMMA'), ('STEMSC', 'STEMSC')], default='HUMSS', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(default='subj', max_length=250)),
                ('teacher_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.teacher')),
            ],
        ),
    ]
