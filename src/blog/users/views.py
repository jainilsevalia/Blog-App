from django.shortcuts import render, redirect 
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('signin')
    else:
        form = UserRegisterForm()

    return render(request, 'user/signup.html', {'form': form })

@login_required
def profile(request):
    return render(request, 'user/profile.html')
