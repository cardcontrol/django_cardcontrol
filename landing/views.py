

# Create your views here.
from django.shortcuts import render
import random
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

def index(request):
  background_color = '#abd3f7' 
  context = {'background_color': background_color}  # Empty context dictionary for now
  return render(request, 'index.html', context)
  
  
def signup(request):
  if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid(): 
          User = get_user_model()  # Get the custom user model
          user = form.save(commit=False)
          user.set_password(form.cleaned_data['password'])
          user.save()
          login(request, user)
          return redirect('landing')  # Replace 'landing' with your desired redirect URL
  else:
      form = SignUpForm()
  return render(request, 'signup.html', {'form': form})


def landing(request):
    # Your landing page logic here
    return render(request, 'landing.html')
  
def blog(request):
    # Your blog logic here
    return render(request, 'blog.html')  # Replace with your blog template

def my_account(request):
    # Your account logic here
    return render(request, 'my_account.html')  # Replace with your account template
  
def home(request):
    return redirect('landing')  # Redirect to the landing page named url

def login(request):
    return render(request, 'login.html')  # Redirect to the landing page named url

