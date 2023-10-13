from django.shortcuts import render
from django.http import HttpResponse
from .models import List
from django.core.mail import send_mail

def home(request):
    return render(request,"first.html")

def placements(request):
    return render(request,"placement.html")
def mocktest(request):
    return render(request,"mock-test.html")
def submit(request):
    return render(request,"submit.html")
def tests(request):
    return render(request, "tests.html")
def footer(request):
    return render(request,"footer.html")
def press(request):
    #if request.method=="POST":
    obj=List.objects.all()
    return render(request,"base.html",{'obj':obj})
def checkEligibility(request):
    return render(request,"list.html")
        
def cgpaa(request):       
        if request.method=="POST":
            cgpa=float(request.POST["cgpa"])
            if cgpa>8:
                obj=List.objects.all()
                return render(request,"base.html",{'obj':obj})
            else:
                return HttpResponse("Sorry! Your are not eligible")
 
 
 
 
def contact(request):
    if request.method=="POST":
        fname=request.POST['fname']
        #body=request.POST['body']
        email=request.POST['email']
        #body=request.POST['body']
        send_mail(
        "Registration Successful 🚀",
        "Hey "+fname +",😃\nYour registration for Mock Interview is successful. We are so glad that you took a step ahead in your life by applying for the mock interview. We will contact you shortly about the time slot ⏱️. It would be even better if you replied with your preferred time slot to this email.\n\nThank you for your patience.\n\nRegards\nGVPCEW",
        'gvpcewcollege@gmail.com',  #frommail
        [email],  #to mail
        fail_silently=False 
        
        
        )
    
        return HttpResponse("yes!!!! mail sent")
    
    else:
       return HttpResponse(" mail not sent")              
            
            
            
            
            