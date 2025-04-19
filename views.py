from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully.")
            return redirect('register')
        else:
            messages.error(request, "There was an error in your form.")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
