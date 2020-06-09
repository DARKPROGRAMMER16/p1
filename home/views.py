from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home/home.html')
    # return HttpResponse('this is home')
def contact(request):
    messages.success(request,'Welcome to contact.')
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if(len(name)<2 or len(email)<5 or len(phone)<8 or len(content)<5):
            messages.error(request,'Your form cannot be filled. Please fill it with correct value.')
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Your form has been submitted successfully.')


    return render(request,'home/contact.html')
    # return HttpResponse('this is contact')
def about(request):
    return render(request,'home/about.html')
    # return HttpResponse('this is about')