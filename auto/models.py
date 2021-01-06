from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from django_countries.fields import CountryField
import os


class Profile(models.Model):
    STATUS_CHOICES = (
        ('man', 'Мужчина'),
        ('woman', 'Женщина'),
    )
    DOC_TYPE = (
        ('passport', 'Паспорт'),
        ('internationalPassport', 'Загран-паспорт'),
        ('certification', 'Свидетельство')
    )
    TYPE_OF_SETTLEMENT = (
        ('city', 'Город'),
        ('urbanSettlement', 'Городское поселение'),
        ('villagie', 'Село'),
        ('village', 'Поселок'),
        ('urbanTypeSettlement', 'Поселок городского типа'),
    )
    userClient = models.CharField(max_length=20 ,verbose_name="Логин")
    # user = models.DateTimeField(str(datetime.now())[0:16].replace(":", ""))
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, verbose_name="Имя")
    sirName = models.CharField(max_length=50, blank=True, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=30, verbose_name="Отчество/по паспорту")
    sex = models.CharField(max_length=30, blank=True, choices=STATUS_CHOICES, default='Мужчина', verbose_name="Пол")
    birthDate = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    country = CountryField(blank_label='(Выберите страну)', verbose_name="Гражданство")
    docs = models.CharField(max_length=30, blank=True, choices=DOC_TYPE, default='Паспорт', verbose_name="Документ")
    docNumber = models.CharField(max_length=50, blank=True, verbose_name="Номер документа")
    gave = models.CharField(max_length=50, blank=True, verbose_name="Кем выдан")
    date = models.DateField(blank=True, verbose_name="Дата выдачи")
    inn = models.CharField(max_length=25, blank=True, verbose_name="ИНН")
    postalCode = models.CharField(max_length=30, blank=True, verbose_name="индекс")
    region = models.CharField(max_length=50, verbose_name="Регион")
    district = models.CharField(max_length=50, verbose_name="Район")
    settlement = models.CharField(max_length=30, choices=TYPE_OF_SETTLEMENT, default='Город',
                                  verbose_name="Название населенного пункта")
    settlementName = models.CharField(max_length=50, blank=True, verbose_name="Название населенного пункта")
    street = models.CharField(max_length=50, blank=True, verbose_name="Название улицы")
    buildingNumber = models.CharField(max_length=10, blank=True, verbose_name="Номер дома")
    housing = models.CharField(max_length=20, verbose_name="Корпус")
    apartment = models.CharField(max_length=20, blank=True, verbose_name="Квартира")
    phoneNumber = models.CharField(max_length=50, verbose_name="Телефонный номер")
    location = models.CharField(max_length=30, blank=True, verbose_name="Регион/Область")
    city = models.CharField(max_length=50, blank=True, verbose_name="Город")
    carCost = models.CharField(max_length=50, verbose_name="Стоимость авто")

    postalCode_f = models.CharField(max_length=30, blank=True, verbose_name="индекс")
    region_f = models.CharField(max_length=50, verbose_name="Регион")
    district_f = models.CharField(max_length=50, verbose_name="Район")
    settlement_f = models.CharField(max_length=30, choices=TYPE_OF_SETTLEMENT, default='Город',
                                    verbose_name="Название населенного пункта")
    settlementName_f = models.CharField(max_length=50, blank=True, verbose_name="Название населенного пункта")
    street_f = models.CharField(max_length=50, blank=True, verbose_name="Название улицы")
    buildingNumber_f = models.CharField(max_length=10, blank=True, verbose_name="Номер дома")
    housing_f = models.CharField(max_length=20, verbose_name="Корпус")
    apartment_f = models.CharField(max_length=20, verbose_name="Квартира")

    employmentType = models.CharField(max_length=20, blank=True, verbose_name="Тип занятости")
    income = models.IntegerField(blank=True,
                                 verbose_name="Среднемесячный доход за последние 6 месяцев за вычетом налогов, сом")
    familyIncome = models.IntegerField(blank=True,
                                       verbose_name="Среднемесячный совокупный доход семьи за последние 6 месяцев, сом")

    password = models.CharField(max_length=255, blank=True, verbose_name="Пароль")
    passwordRepeat = models.CharField(max_length=255, blank=True, verbose_name="Повторите пароль")
    phoneNumber2 = models.CharField(max_length=150, blank=True, verbose_name="Номер телефона")
    phoneNumberSub = models.CharField(max_length=150, verbose_name="Дополнительный номер")
    secretWord = models.CharField(max_length=150, blank=True, verbose_name="Секретное слово")

    #Оплата рассрочки


    class Meta:
        verbose_name="Клиент"
        verbose_name_plural="Клиенты"
    # def __str__(self):
    #     return 'Profile for user {}'.format(self.user.username)


class Partner(models.Model):
    userPartner = models.CharField(max_length=20, verbose_name="Логин")
    # userPartner = models.DateTimeField(str(datetime.now())[0:16].replace(":", ""))
    namePartner = models.CharField(max_length=50, blank=True, verbose_name="Имя")
    sirNamePartner = models.CharField(max_length=50, blank=True, verbose_name="Фамилия")
    patronymicPartner = models.CharField(max_length=30, verbose_name="Отчество/по паспорту")
    phonePartner = models.CharField(max_length=50, blank=True, verbose_name="Телефонный номер")
    emailPartner = models.EmailField(max_length=50, blank=True, verbose_name="Email")
    adressPartner = models.CharField(max_length=150, blank=True, verbose_name="Адрес")
    secretWordPartner = models.CharField(max_length=150, blank=True, verbose_name="Секретное слово")
    passwordPartner = models.CharField(max_length=255, blank=True, verbose_name="Пароль")
    passwordRepeatPartner = models.CharField(max_length=255, blank=True, verbose_name="Повторите пароль")
    docNumberPartner = models.CharField(max_length=50, blank=True, verbose_name="Номер документа")
    gavePartner = models.CharField(max_length=50, blank=True, verbose_name="Кем выдан")
    datePartner = models.DateField(blank=True, verbose_name="Дата выдачи")
    upload = models.FileField(upload_to='uploads/', verbose_name="Прикрепить файл")


    class Meta:
        verbose_name="Партнер"
        verbose_name_plural="Партнеры"
    # def __str__(self):
    #     return 'Partner for user {}'.format(self.user.username)
