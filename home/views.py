from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.
def home(request):
    allpost = Post.objects.all()
    context = {'allpost':allpost}
    return render(request,'home/home.html',context)
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

def search(request):
    query = request.GET['query']
    if len(query)<3:
        apost = Post.objects.none()
    else:
        aposttitle = Post.objects.filter(title__icontains=query)
        apostcontent = Post.objects.filter(content__icontains=query)
        apost = aposttitle.union(apostcontent)
    if apost.count() == 0:
        messages.warning(request,"No search result found. ")
    params = {'apost':apost,'query':query}
    return render(request,'home/search.html',params)
    # return HttpResponse('this is search')

def handlesignup(request):
    if request.method == 'POST':
        #get the post parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        femail = request.POST['femail']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for errorneous input
        if len(username)>15:
            messages.error(request,"username must be 15 characters.")
            return redirect('home')
        if not username.isalnum():
            messages.error(request,"username must contain only numbers and letters")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request,"password didnt match")
            return redirect('home')



        #create the user
        myuser = User.objects.create_user(username,femail,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"your account has been succesfully created.")
        return redirect('home')
    else:
        return HttpResponse("404 - Not found")

def handlelogin(request):
    if request.method == 'POST':
        lgusername = request.POST['lgusername']
        lgpass = request.POST['lgpass']

        user = authenticate(username = lgusername, password = lgpass)

        if user is not None:
            login(request,user)
            messages.success(request,"succesfully logged in")
            return redirect('home')
        else:
            messages.error(request,"invalid credentials, please try again")
            return redirect('home')
    
    return HttpResponse("404 - Not found")

def handlelogout(request):
    logout(request)
    messages.success(request,"you are successfully logged out.")
    return redirect('home')
    