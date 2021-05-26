from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method== 'POST':
        login_data = request.POST.dict()
        username = login_data.get("Username")
        password = login_data.get("Password")
        print(username, password)
        if username == "akshay" and  password == "z333":
            return render(request,'drpg.html')
        else:
            messages.error(request, 'Document deleted.')
            return HttpResponse('invalid username or password')
    else:
        return render(request,'login.html')
    
        


    # if username.lower()=="akshay" and password=="zoro999":
    #     return render(request,'drpg.html')    
    # else:
    #     return render(request,'login.html')
        
    
# def login(request):
#     return render(request,'login.html')


def Dr(request):
    return render(request,'drpg.html')