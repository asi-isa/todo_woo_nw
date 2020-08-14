from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

def signup_user(request):
    if request.method == 'GET':
        return render(request, 'signup_user.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current_todos')
            except IntegrityError:
                err_integrity = "That username has already been taken. please try_again"
                return render(request, 'signup_user.html', {'form': UserCreationForm(), 'err_integrity': err_integrity})
        else:
            err_passw_missmatch = "your passwords didn't match. please try_again"
            return render(request, 'signup_user.html', {'form': UserCreationForm(), 'err_passw_missmatch': err_passw_missmatch})



