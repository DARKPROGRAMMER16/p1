from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages
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