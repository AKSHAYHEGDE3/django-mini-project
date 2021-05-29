from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Patient
# Create your views here.
# def patient(request):
#     return render(request,'patient.html')

def patient(request):
     # retrieving details from form and putting details in a dict.
     if request.method == 'POST':
          pt_data = request.POST.dict()
          par={'name': pt_data.get('patient_name'),
               'mobile_no':pt_data.get('patient_mobile_no'),
               'email_id':pt_data.get('patient_email'),
               'appointment_date':pt_data.get('patient_appointment'),
               }
          
          #check if appointment is available
          pts=Patient.objects.all()
          y=pts.filter(patient_appointment=par['appointment_date'])
          if len(y) > 9:
               return HttpResponse('Appointment on this day is full, please choose another date')
          else : 
               #saving data to database
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





     

     

