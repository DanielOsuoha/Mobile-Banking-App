from django.shortcuts import render
from user_auth.forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def signUp(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f"Hey {username}, your account was created successfully.")
            new_user = authenticate(username=email, password=password) 
            login(request, new_user)
            return render(request, "core/index.html")
    else:
        form = UserForm()
    if request.user.is_authenticated:
        messages.warning(request, f"{request.user.username}, you are already logged in. Log out to create a new account.")
        return render(request, "core/index.html")
    context = {
        "form": form
    }    
    return render(request, "user_auth/signup.html", context)

