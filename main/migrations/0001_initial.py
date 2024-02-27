# Generated by Django 5.0.2 on 2024-02-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название экскурсии')),
                ('desc', models.TextField(verbose_name='Описание экскурсии')),
                ('time', models.TimeField(verbose_name='Время начала экскурсии')),
            ],
        ),
    ]