from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()
   # check if logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home')
        else:
            messages.error(request, "There is a problem login in, please try again.")
            return redirect('home')
    else:
        return render(request, "home.html", {'records': records})



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        # create a new user
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

        # authenticate and login
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully registred!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, "register.html", {'form': form})


def record_details(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, "record.html", {'record': record})
    else:
        messages.error(request, "You must be logged in to see the record")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, 'The record was deleted.')
        return redirect('home')
    else:
        messages.error(request, "You must be logged in to see the record")
        return redirect('home')


def add_record(request):
    if request.method == "POST":
        # create a new record
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'The record was successfully added.')
        return redirect('home')
    form = AddRecordForm()
    return render(request, "add_record.html", {'form': form})



def edit_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated")
            return redirect('home')
            form = AddRecordForm()
        return render(request, "edit_record.html", {'form': form})
    else:
        messages.error(request, "You must be logged to update a record")
        return redirect('home')






