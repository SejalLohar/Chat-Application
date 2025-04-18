from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        print("Form submitted:", request.POST)  # Debug print
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debug print
            # In a real application, we would validate credentials here
            return redirect(reverse('chat'))
        else:
            print("Form errors:", form.errors)  # Debug print
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def chat_view(request):
    return render(request, 'chat.html')
