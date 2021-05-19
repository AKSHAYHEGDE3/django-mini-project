from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient
# Create your views here.
# def patient(request):
#     return render(request,'patient.html')

def patient(request):
        if request.method == 'POST':
             pt_data = request.POST.dict()
             par={'name': pt_data.get('patient_name'),
                  'mobile_no':pt_data.get('patient_mobile_no'),
                  'email_id':pt_data.get('patient_email'),
                  'appointment_date':pt_data.get('patient_appointment'),
                  }
             if request.POST.get('patient_name') and request.POST.get('patient_mobile_no') and request.POST.get('patient_email') :
                post=Patient()
                post.patient_id= request.POST.get('patient_id')
                post.patient_name= request.POST.get('patient_name')
                post.patient_mobile_no= request.POST.get('patient_mobile_no')
                post.patient_email= request.POST.get('patient_email')
                post.patient_appointment= request.POST.get('patient_appointment')
                post.save()
               
                return render(request, 'success.html',par)
        else:
            return render(request,'patient.html')
def success(request):
    return render(request,'success.html')



       
                


     

     

