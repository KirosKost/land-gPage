from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from django_countries.fields import CountryField
import os

# Модель регистрации клиента

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

# Клиенты какого либо партнера
# class UserList(models.Model):
#     first_name = models.CharField(max_length=200, blank=True, verbose_name="Имя")
#     last_name = models.CharField(max_length=200, blank=True, verbose_name="Фамилия")
    
#     class Meta:
#         verbose_name="Мой клиент"
#         verbose_name_plural="Мои клиенты"

# Модель регистрации партнера
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


class Ads(models.Model):

    ads = models.TextField(max_length=500,verbose_name="Содержание")

    class Meta:
        verbose_name="Объявление"
        verbose_name_plural="Объявления"


# Поля об акциях для клиентов и партнеров
class SharesFirst(models.Model):
    SharesTitle = models.CharField(max_length=50,verbose_name="Название")
    SharesUpload = models.FileField(upload_to='uploads/', verbose_name="Выбрать файл")
    SharesDateStart = models.DateTimeField(blank=True, verbose_name="Начало")
    SharesDateEnd = models.DateTimeField(blank=True, verbose_name="Конец")
    ClientsShares = models.TextField(max_length=500,verbose_name="Акции для клиентов")

    class Meta:
        verbose_name="Акции для клиентов"
        verbose_name_plural="Акции для клиентов"


class SharesSecond(models.Model):
    SharesTitleSecond = models.CharField(max_length=50,verbose_name="Название")
    SharesUploadSecond = models.FileField(upload_to='uploads/', verbose_name="Выбрать файл")
    SharesDateStartSecond = models.DateTimeField(blank=True, verbose_name="Начало")
    SharesDateEndSecond = models.DateTimeField(blank=True, verbose_name="Конец")
    PartnersSharesSecond = models.TextField(max_length=500,verbose_name="Акции для клиентов")

    class Meta:
        verbose_name="Акции для партнеров"
        verbose_name_plural="Акции для партнеров"        

class Lawyer(models.Model):
    lawyerName = models.CharField(max_length=50,verbose_name="Имя")
    lawyerSirName = models.CharField(max_length=50, verbose_name="Фамилия")
    lawyerPatronymic = models.CharField(max_length=50,verbose_name="Отчество")
    lawyerEmail = models.EmailField(max_length=50, blank=True, verbose_name="Адрес электронной почты")
    lawyerPhoneNUmber = models.CharField(max_length=50, verbose_name="Телефон")
    lawyerPassword = models.CharField(max_length=255, blank=True, verbose_name="Пароль")
    lawyerPasswordRepeat = models.CharField(max_length=255, blank=True, verbose_name="Повторите пароль")

    class Meta:
        verbose_name="Юрист"
        verbose_name_plural="Юрист"    

class Accountant(models.Model):
    accountantName = models.CharField(max_length=50,verbose_name="Имя")
    accountantSirName = models.CharField(max_length=50, verbose_name="Фамилия")
    accountantPatronymic = models.CharField(max_length=50,verbose_name="Отчество")
    accountantEmail = models.EmailField(max_length=50, blank=True, verbose_name="Адрес электронной почты")
    accountantPhoneNUmber = models.CharField(max_length=50, verbose_name="Телефон")
    accountantPassword = models.CharField(max_length=255, blank=True, verbose_name="Пароль")
    accountantPasswordRepeat = models.CharField(max_length=255, blank=True, verbose_name="Повторите пароль")
    class Meta:
        verbose_name="Бухгалтер"
        verbose_name_plural="Бухгалтер"           