from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def signUp(request):
    form = UserCreationForm()
    registered = False
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            registered  = True
    dict = {'form': form,'registered': registered}
    return render(request, 'App_login/signup.html', context=dict)    
        


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    dict = {'form': form}
    return render(request, 'App_login/login.html', context=dict) 


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
