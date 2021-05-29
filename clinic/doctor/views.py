from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from datetime import date
# from patient.models import Patient

# Create your views here.


def login(request):
    # patient_list=Patient.objects.all()
    # todays_list=patient_list.filter(patient_appointment=date.today())
    # print(todays_list)
    # print(len(todays_list))
    #data = [{'name': ps.patient_name,'mobile': ps.patient_mobile_no,} for ps in todays_list]
    if request.method == 'POST':
        login_data = request.POST.dict()
        username = login_data.get("Username")
        password = login_data.get("Password")
        #print(username, password)
        if username.lower() == "akshay" and  password == "zoro333":
            return render(request,'drpg.html')
        else:
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
