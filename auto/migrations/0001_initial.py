# Generated by Django 3.1.5 on 2021-01-10 07:25

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accountant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountantName', models.CharField(max_length=50, verbose_name='Имя')),
                ('accountantSirName', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('accountantPatronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('accountantEmail', models.EmailField(blank=True, max_length=50, verbose_name='Адрес электронной почты')),
                ('accountantPhoneNUmber', models.CharField(max_length=50, verbose_name='Телефон')),
                ('accountantPassword', models.CharField(blank=True, max_length=255, verbose_name='Пароль')),
                ('accountantPasswordRepeat', models.CharField(blank=True, max_length=255, verbose_name='Повторите пароль')),
            ],
            options={
                'verbose_name': 'Бухгалтер',
                'verbose_name_plural': 'Бухгалтер',
            },
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ads', models.TextField(max_length=500, verbose_name='Содержание')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lawyerName', models.CharField(max_length=50, verbose_name='Имя')),
                ('lawyerSirName', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('lawyerPatronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('lawyerEmail', models.EmailField(blank=True, max_length=50, verbose_name='Адрес электронной почты')),
                ('lawyerPhoneNUmber', models.CharField(max_length=50, verbose_name='Телефон')),
                ('lawyerPassword', models.CharField(blank=True, max_length=255, verbose_name='Пароль')),
                ('lawyerPasswordRepeat', models.CharField(blank=True, max_length=255, verbose_name='Повторите пароль')),
            ],
            options={
                'verbose_name': 'Юрист',
                'verbose_name_plural': 'Юрист',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userPartner', models.CharField(max_length=20, verbose_name='Логин')),
                ('namePartner', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('sirNamePartner', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('patronymicPartner', models.CharField(max_length=30, verbose_name='Отчество/по паспорту')),
                ('phonePartner', models.CharField(blank=True, max_length=50, verbose_name='Телефонный номер')),
                ('emailPartner', models.EmailField(blank=True, max_length=50, verbose_name='Email')),
                ('adressPartner', models.CharField(blank=True, max_length=150, verbose_name='Адрес')),
                ('secretWordPartner', models.CharField(blank=True, max_length=150, verbose_name='Секретное слово')),
                ('passwordPartner', models.CharField(blank=True, max_length=255, verbose_name='Пароль')),
                ('passwordRepeatPartner', models.CharField(blank=True, max_length=255, verbose_name='Повторите пароль')),
                ('docNumberPartner', models.CharField(blank=True, max_length=50, verbose_name='Номер документа')),
                ('gavePartner', models.CharField(blank=True, max_length=50, verbose_name='Кем выдан')),
                ('datePartner', models.DateField(blank=True, verbose_name='Дата выдачи')),
                ('upload', models.FileField(upload_to='uploads/', verbose_name='Прикрепить файл')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userClient', models.CharField(max_length=20, verbose_name='Логин')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('sirName', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=30, verbose_name='Отчество/по паспорту')),
                ('sex', models.CharField(blank=True, choices=[('man', 'Мужчина'), ('woman', 'Женщина')], default='Мужчина', max_length=30, verbose_name='Пол')),
                ('birthDate', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='Гражданство')),
                ('docs', models.CharField(blank=True, choices=[('passport', 'Паспорт'), ('internationalPassport', 'Загран-паспорт'), ('certification', 'Свидетельство')], default='Паспорт', max_length=30, verbose_name='Документ')),
                ('docNumber', models.CharField(blank=True, max_length=50, verbose_name='Номер документа')),
                ('gave', models.CharField(blank=True, max_length=50, verbose_name='Кем выдан')),
                ('date', models.DateField(blank=True, verbose_name='Дата выдачи')),
                ('inn', models.CharField(blank=True, max_length=25, verbose_name='ИНН')),
                ('postalCode', models.CharField(blank=True, max_length=30, verbose_name='индекс')),
                ('region', models.CharField(max_length=50, verbose_name='Регион')),
                ('district', models.CharField(max_length=50, verbose_name='Район')),
                ('settlement', models.CharField(choices=[('city', 'Город'), ('urbanSettlement', 'Городское поселение'), ('villagie', 'Село'), ('village', 'Поселок'), ('urbanTypeSettlement', 'Поселок городского типа')], default='Город', max_length=30, verbose_name='Название населенного пункта')),
                ('settlementName', models.CharField(blank=True, max_length=50, verbose_name='Название населенного пункта')),
                ('street', models.CharField(blank=True, max_length=50, verbose_name='Название улицы')),
                ('buildingNumber', models.CharField(blank=True, max_length=10, verbose_name='Номер дома')),
                ('housing', models.CharField(max_length=20, verbose_name='Корпус')),
                ('apartment', models.CharField(blank=True, max_length=20, verbose_name='Квартира')),
                ('phoneNumber', models.CharField(max_length=50, verbose_name='Телефонный номер')),
                ('location', models.CharField(blank=True, max_length=30, verbose_name='Регион/Область')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='Город')),
                ('carCost', models.CharField(max_length=50, verbose_name='Стоимость авто')),
                ('postalCode_f', models.CharField(blank=True, max_length=30, verbose_name='индекс')),
                ('region_f', models.CharField(max_length=50, verbose_name='Регион')),
                ('district_f', models.CharField(max_length=50, verbose_name='Район')),
                ('settlement_f', models.CharField(choices=[('city', 'Город'), ('urbanSettlement', 'Городское поселение'), ('villagie', 'Село'), ('village', 'Поселок'), ('urbanTypeSettlement', 'Поселок городского типа')], default='Город', max_length=30, verbose_name='Название населенного пункта')),
                ('settlementName_f', models.CharField(blank=True, max_length=50, verbose_name='Название населенного пункта')),
                ('street_f', models.CharField(blank=True, max_length=50, verbose_name='Название улицы')),
                ('buildingNumber_f', models.CharField(blank=True, max_length=10, verbose_name='Номер дома')),
                ('housing_f', models.CharField(max_length=20, verbose_name='Корпус')),
                ('apartment_f', models.CharField(max_length=20, verbose_name='Квартира')),
                ('employmentType', models.CharField(blank=True, max_length=20, verbose_name='Тип занятости')),
                ('income', models.IntegerField(blank=True, verbose_name='Среднемесячный доход за последние 6 месяцев за вычетом налогов, сом')),
                ('familyIncome', models.IntegerField(blank=True, verbose_name='Среднемесячный совокупный доход семьи за последние 6 месяцев, сом')),
                ('password', models.CharField(blank=True, max_length=255, verbose_name='Пароль')),
                ('passwordRepeat', models.CharField(blank=True, max_length=255, verbose_name='Повторите пароль')),
                ('phoneNumber2', models.CharField(blank=True, max_length=150, verbose_name='Номер телефона')),
                ('phoneNumberSub', models.CharField(max_length=150, verbose_name='Дополнительный номер')),
                ('secretWord', models.CharField(blank=True, max_length=150, verbose_name='Секретное слово')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='SharesFirst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SharesTitle', models.CharField(max_length=50, verbose_name='Название')),
                ('SharesUpload', models.FileField(upload_to='uploads/', verbose_name='Выбрать файл')),
                ('SharesDateStart', models.DateTimeField(blank=True, verbose_name='Начало')),
                ('SharesDateEnd', models.DateTimeField(blank=True, verbose_name='Конец')),
                ('ClientsShares', models.TextField(max_length=500, verbose_name='Акции для клиентов')),
            ],
            options={
                'verbose_name': 'Акции для клиентов',
                'verbose_name_plural': 'Акции для клиентов',
            },
        ),
        migrations.CreateModel(
            name='SharesSecond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SharesTitleSecond', models.CharField(max_length=50, verbose_name='Название')),
                ('SharesUploadSecond', models.FileField(upload_to='uploads/', verbose_name='Выбрать файл')),
                ('SharesDateStartSecond', models.DateTimeField(blank=True, verbose_name='Начало')),
                ('SharesDateEndSecond', models.DateTimeField(blank=True, verbose_name='Конец')),
                ('PartnersSharesSecond', models.TextField(max_length=500, verbose_name='Акции для клиентов')),
            ],
            options={
                'verbose_name': 'Акции для партнеров',
                'verbose_name_plural': 'Акции для партнеров',
            },
        ),
    ]
