from django.shortcuts import render ,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None :
            auth.login(request,user)
            messages.success(request , 'you are login now ')
            return redirect ('url_dashboard')
        else :
            messages.error(request,'your login faild')
            return redirect('url_login')

    else:
        return render(request , 'accounts/login.html')

def register(request):
    if request.method == "POST" :
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error (request,'passwords dose not math')
            return redirect ('url_register')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'username already exists')
            return redirect('url_register')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'email already exists')
            return redirect('url_register')
        else :
            user = User.objects.create_user(username=username , first_name=firstname , last_name=lastname , email=email , password=password)
            auth.login (request,user)
            messages.success(request, 'you are login now ')
            return redirect ('url_dashboard')
            user.save()
            messages.success(request , 'you are registered successfully.')
            return redirect('url_login')
    else:
        return render(request , 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request , 'you are successfully')
        return redirect('home')
    return redirect('home')

def dashboard(request):
    return render(request , 'accounts/dashboard.html')
