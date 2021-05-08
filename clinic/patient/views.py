from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient

# Create your views here.
# def patient(request):
#     return render(request,'patient.html')

def patient(request):
        if request.method == 'POST':
             if request.POST.get('patient_name') and request.POST.get('patient_mobile_no') and request.POST.get('patient_email') :
                post=Patient()
                post.patient_name= request.POST.get('patient_name')
                post.patient_mobile_no= request.POST.get('patient_mobile_no')
                post.patient_email= request.POST.get('patient_email')
                #post.patient_appointment= request.POST.get('patient_appointment')
                post.save() 
                return render(request, 'success.html')
        else:
            return render(request,'patient.html')
def success(request):
    return render(request,'success.html')


            
                 

       
                


     

     

