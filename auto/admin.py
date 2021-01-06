from django.contrib import admin
from .models import *



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['userClient', 'name', 'sirName', 'patronymic', 'sex', 'birthDate', 'country', 'docs',
                    'docNumber', 'gave', 'date', 'inn', 'postalCode', 'region', 'district', 'settlement',
                    'settlementName', 'street', 'buildingNumber', 'housing', 'apartment', 'phoneNumber',
                    'location', 'city', 'carCost', 'postalCode_f', 'region_f', 'district_f', 'settlement_f', 'settlementName_f',
                    'street_f', 'buildingNumber_f', 'housing_f', 'apartment_f', 'employmentType', 'income', 'familyIncome',
                    'password', 'phoneNumber2', 'phoneNumberSub', 'secretWord']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['userPartner' ,'namePartner', 'sirNamePartner', 'patronymicPartner', 'phonePartner', 'emailPartner',
                  'adressPartner', 'secretWordPartner', 'passwordPartner', 'passwordRepeatPartner', 'docNumberPartner',
                  'gavePartner', 'datePartner', 'upload']
