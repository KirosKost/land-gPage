# Generated by Django 3.1.5 on 2021-01-11 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0003_auto_20210110_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='ФИО')),
                ('phoneNumber', models.CharField(max_length=100, verbose_name='Номер телефона')),
                ('text', models.TextField(verbose_name='Сообщение')),
            ],
        ),
    ]
