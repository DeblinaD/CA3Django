from django.shortcuts import render,redirect
from .forms import UserForm, RecordForm,SignUpForm, LoginForm
from .models import Record,User
from datetime import date
from django.db.models import Sum,Avg
# views.py

from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('record')
            else:
                # Return an 'invalid login' error message.
                error_message = "Invalid username or password."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('record')  # Redirect to the homepage after logout



def user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user_form.save()
              # Redirect to success page
    else:
        user_form = UserForm()
    return render(request, 'userform.html', {'user_form': user_form})

def name(request):
    
    user_name = ''  # Initialize user_name to an empty string

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                user_name = user.Name
            except User.DoesNotExist:
                user_name = 'User Not Found'

    return user_name  
  

def record(request):  
    user_name = name(request)
    if request.method == 'POST':
        record_form = RecordForm(request.POST)
        if record_form.is_valid():
            record_form.save() 
            record_form = RecordForm()      
    else:
        record_form = RecordForm()

    data = Record.objects.filter(Date=date.today())
    return render(request, 'record.html', {'record_form': record_form, 'data': data, 'user_name': user_name })
    



def total(request):
    submit = None
    total_quantity = None
    average_fat = None
    total_amount = None
    if request.method == "POST":
        user = request.POST.get('User')  # Assuming you want to filter by user as well
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        submit = Record.objects.filter(user_id=user,Date__range=(fromdate, todate))
        total_quantity = submit.aggregate(total_quantity=Sum('Quantity'))['total_quantity']
        average_fat = submit.aggregate(average_fat=Avg('Fat'))['average_fat']
        total_amount = submit.aggregate(total_amount=Sum('Amount'))['total_amount']
    return render(request, 'total.html', {'submit': submit,'total_amount': total_amount,'total_quantity': total_quantity,'average_fat':average_fat})

def visual(request):
    return render(request, 'visual.html')