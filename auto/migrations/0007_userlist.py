# Generated by Django 3.1.5 on 2021-01-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0006_makeapayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=200, verbose_name='Фамилия')),
            ],
            options={
                'verbose_name': 'Мой клиент',
                'verbose_name_plural': 'Мои клиенты',
            },
        ),
    ]
