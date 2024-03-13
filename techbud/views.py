from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from techbud.models import*

# Create your views here.
@login_required(login_url='/login_logic/')
def home(request): 
    print(request.user.is_authenticated)
    return render(request, 'home.html')
def base(request):
    return render(request, 'base.html')

def sign_up(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        uemail = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("confirm")
        if pass1 == pass2:
             my_user = User.objects.create_user(uname, uemail, password=pass1)
             my_user.save()
             return redirect('login_view')
        else:
            return HttpResponse("Error in password")
    return render(request, 'Signup.html')
def login_view(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        web_user = authenticate(request, username = user_name , password = pass_word)
        if web_user is not None:
            login(request, web_user)
            return redirect('home')
        else:
            return HttpResponse("Username or pass incorrect")
    return render(request, 'login.html')
def logout_page(request):
    logout(request)
    return redirect('login_view')
def aboutpage(request):
    return render(request, 'about.html')
def smart_phone(request):
    if request.method == 'POST':
        brand = request.POST.get('brand')
        budget_range = request.POST.get('budget')
        if brand == 'Samsung' and budget_range == '10k-20k':
            mobile = Mobile.objects.filter(brand_name = brand , budget_range=budget_range)
            if mobile:
                return render(request, 'result.html' ,{'mobile': mobile})
        elif brand == 'Redmi' and budget_range == '10k-20k':
            mobile = Mobile.objects.filter(brand_name = brand , budget_range=budget_range)
            if mobile:
                return render(request, 'result.html' , {'mobile': mobile})
        else:
            return HttpResponse("Failure")
    return render(request,'phone.html')
def search_items(request):
    if request.method =='GET':
        query = request.GET.get('query', '')
        results = Mobile.objects.all().filter(brand_name__icontains =query)
        return render(request, 'results.html', {'query' : query , 'results' : results})
