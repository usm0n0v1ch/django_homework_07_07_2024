# Generated by Django 4.2.16 on 2024-09-09 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_vacancy_response_response_vacancy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='vacancy',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.response'),
        ),
    ]