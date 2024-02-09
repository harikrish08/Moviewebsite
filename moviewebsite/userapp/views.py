from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from userapp.form import profileform


# Create your views here.
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['password']
        pwd1 = request.POST['password1']
        if pwd == pwd1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('userapp:registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Registered Already')
                return redirect('userapp:registration')
            else:
                user = User.objects.create_user(username=username, first_name=f_name, last_name=l_name, email=email,
                                                password=pwd)
                user.save();
                print('User Created')
                messages.info(request, 'Registration successful. Welcome, ' + username + '!')
                return redirect('userapp:login')

        else:
            messages.info(request, 'Passwords Not Matching')
            return redirect('userapp:registration')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/movie')
        else:
            print('Invalid User')
            return redirect('userapp:login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/movie')


def profile(request):
    user = request.user
    username = user.username
    first_name = user.first_name
    last_name = user.last_name
    email = user.email

    return render(request, 'profile.html',
                  {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email})


def updateprofile(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = profileform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('/movie')
    else:
        form = profileform(instance=user)
    return render(request, 'updatepro.html', {'form': form})
