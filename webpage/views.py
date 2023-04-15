from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def staffRegister(request):
    if request.method == 'POST' or None:
        form = NewStaffForm(request.POST)
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'That email is already in use')
        
        elif form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "you have registered successfully")
            return redirect('staff')
        else:
            messages.error(request, "There was an error, please try again later")
    form = NewStaffForm()
    return render(request=request, template_name='webpage/register.html', context={'form': form})

          
def staffLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in {username}')
                return redirect('staff')
            else:
                messages.error(request, 'invalid username or password')
        else:
            messages.error(request, 'invalid username or password')
    form = AuthenticationForm()
    return render(request=request, template_name="webpage/login.html", context={'form': form})


def staffLogout(request):
    logout(request)
    messages.info(request, 'staff logout')
    return redirect('login')


                                        
def home(request):
    return render(request, 'webpage/home.html', context={})


def contact(request):
    return render(request, 'webpage/contact.html', context={})


def staff(request):
    form = Tanda.objects.all
    redirect_field_name = 'login'
    return render(request, 'webpage/staff.html', context={'form': form})


def issue(request):
    if request.method == 'POST':
        form = TandaForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            complaintType = form.cleaned_data['complaintType']
            complaintDetails = form.cleaned_data['complaintDetails']
            recommendation = form.cleaned_data['recommendation']
            
            try:
             send_mail(email,complaintType,complaintDetails, ["nurudeenolamide010gmail.com"] )
            except BadHeaderError:
             return HttpResponse("Invalid email address")
            return redirect('success')



        return render(request, 'webpage/issue.html', {'form':form})
    else:
            form =TandaForm()
            return render(request, 'webpage/issue.html', {'form':form})
    

def successView(request):
    return render(request, 'webpage/success.html')