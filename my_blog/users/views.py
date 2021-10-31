from django.shortcuts import render, redirect

# import a form for creating a user
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
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
            messages.success(request, f'Account created for {username}!')

            # redirects the user back to the blog's home page after displaying a success message
            return redirect('myBlog-home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form' : form})
