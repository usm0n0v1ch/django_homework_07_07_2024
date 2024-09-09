# Generated by Django 4.2.16 on 2024-09-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('skills', models.TextField()),
                ('experience', models.TextField()),
                ('education', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('required_skills', models.TextField()),
                ('responsibilities', models.TextField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
