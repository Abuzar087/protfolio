from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
   
    return render(request, 'home.html')





from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

def contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"New Contact Form Submission\n\nName: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject=f"Contact Form: {subject}",
                message=full_message,
                from_email="abuzarrao617@gmail.com",  # Your email
                recipient_list=["abuzarrao617@gmail.com"],  # Replace with your email
                fail_silently=False,
            )
            return render(request,'thanku.html')
        except Exception as e:
            return HttpResponse(f"Error sending email: {e}")

    return render(request, "home.html")



