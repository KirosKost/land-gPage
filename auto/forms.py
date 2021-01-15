from django import forms
from django.contrib.auth.models import User
from .models import *
from .models import Feedback


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('userClient', 'name', 'sirName', 'patronymic', 'sex', 'birthDate', 'country', 'docs',
                    'docNumber', 'gave', 'date', 'inn', 'postalCode', 'region', 'district', 'settlement',
                    'settlementName', 'street', 'buildingNumber', 'housing', 'apartment', 'phoneNumber',
                    'location', 'city', 'carCost', 'postalCode_f', 'region_f', 'district_f', 'settlement_f', 'settlementName_f',
                    'street_f', 'buildingNumber_f', 'housing_f', 'apartment_f', 'employmentType', 'income', 'familyIncome',
                    'password', 'passwordRepeat', 'phoneNumber2', 'phoneNumberSub', 'secretWord')


class PartnerEditForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ('userPartner' ,'namePartner', 'sirNamePartner', 'patronymicPartner', 'phonePartner', 'emailPartner',
                  'adressPartner', 'secretWordPartner', 'passwordPartner', 'passwordRepeatPartner', 'docNumberPartner',
                  'gavePartner', 'datePartner', 'upload')



class FeedbackForm(forms.ModelForm):
    class Meta:
	    model = Feedback
	    fields = ['phoneNumber', 'name', 'text']


class VerificationOfDocumentsForm(forms.ModelForm):
    class Meta:
        model = VerificationOfDocuments
        fields = ['applicationForMembership', 'passportSides', 'addressReference']



class MakeAPaymentForm(forms.ModelForm):
    class Meta:
        model = MakeAPayment       
        fields = ['entranceFee', 'dateOfPayment', 'paymentMethod', 'document']



class UserList(forms.ModelForm):
    class Meta:
        model = UserList
        fields = ['first_name', 'last_name']        
        