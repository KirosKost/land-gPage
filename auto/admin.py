from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sirName', 'patronymic', 'sex', 'birthDate', 'country', 'docs',
                    'docNumber', 'gave', 'date', 'inn', 'postalCode', 'region', 'district', 'settlement',
                    'settlementName', 'street', 'buildingNumber', 'housing', 'apartment', 'phoneNumber',
                    'location', 'city', 'carCost', 'postalCode_f', 'region_f', 'district_f', 'settlement_f', 'settlementName_f',
                    'street_f', 'buildingNumber_f', 'housing_f', 'apartment_f', 'employmentType', 'income', 'familyIncome',
                    'password', 'phoneNumber2', 'phoneNumberSub', 'secretWord']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'namePartner', 'sirNamePartner', 'patronymicPartner', 'phonePartner', 'emailPartner',
                  'adressPartner', 'secretWordPartner', 'passwordPartner', 'passwordRepeatPartner', 'docNumberPartner',
                  'gavePartner', 'datePartner', 'upload']


@admin.register(Ads)
class Ads(admin.ModelAdmin):
    list_display = ['ads']

@admin.register(SharesFirst)
class SharesFirst(admin.ModelAdmin):
    list_display = ['SharesTitle', 'SharesUpload', 'SharesDateStart',
                    'SharesDateEnd','ClientsShares']

@admin.register(SharesSecond)
class SharesSecond(admin.ModelAdmin):
    list_display = ['SharesTitleSecond', 'SharesUploadSecond', 'SharesDateStartSecond', 
                    'SharesDateEndSecond','PartnersSharesSecond']


@admin.register(Lawyer)
class Lawyer(admin.ModelAdmin):
    list_display = ['lawyerName', 'lawyerSirName', 'lawyerPatronymic', 'lawyerEmail', 'lawyerPhoneNUmber',
                    'lawyerPassword', 'lawyerPasswordRepeat']

@admin.register(Accountant)
class Accountant(admin.ModelAdmin):
    list_display = ['accountantName', 'accountantSirName', 'accountantPatronymic', 'accountantEmail', 'accountantPhoneNUmber',
                    'accountantPassword', 'accountantPasswordRepeat']


@admin.register(PartnerUsers)
class PartnerUsers(admin.ModelAdmin):
    list_display = ['userPartner']




@admin.register(VerificationOfDocuments)
class VerificationOfDocuments(admin.ModelAdmin):
    list_display = ['applicationForMembership', 'passportSides', 'addressReference']    