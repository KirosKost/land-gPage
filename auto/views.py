from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from django.views import View
from .forms import FeedbackForm


def formuser(request):
    return render(request, 'account/testregister.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'auto/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'auto/dashboard.html',
                  {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'auto/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'auto/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'auto/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@login_required
def editPartner(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        partner_form = PartnerEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and partner_form.is_valid():
            user_form.save()
            partner_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        partner_form = PartnerEditForm(instance=request.user.partner)
    return render(request,
                  'auto/edit.html',
                  {'user_form': user_form,
                   'partner_form': partner_form})




class FeedbackView(View):
    
    def post(self, request):
        
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            phoneNumber = form.cleaned_data['phoneNumber']
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            subject = 'Новое сообщение'
            message = 'Новая заявка!' + '\r\n' + '\r\n' + 'Номер телефона: ' + phoneNUmber + '\r\n' + '\r\n' + 'ФИО:' + name + '\r\n' + 'Сообщение' + text
            bot.send_message(628980737, message)
        return redirect('home')	
