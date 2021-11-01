from django.contrib.auth import login
from django.shortcuts import render, redirect

# import a form for creating a user
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.

def register(request):

    # if we get a request with a POST method, we pass in the received data to the form
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
       
        if form.is_valid():

            # actually create the user
            form.save()

            # form.cleaned_data gives a properly-setup dictionary
            username = form.cleaned_data.get('username')

            # uses a fstream 'f'
            messages.success(request, f'Hey {username}, your account was created. You can now log in!')

            # redirects the user to the login page after displaying a success message
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form' : form})

# adds functionality that the user can't go to the profile view if they aren't logged in
@login_required
def profile(request):
    return render(request, 'users/profile.html')