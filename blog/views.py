from django.shortcuts import render,HttpResponse

# Create your views here.
def bloghome(request):
    # return HttpResponse('this is blog home')
    return render(request,'blog/bloghome.html')
def blogpost(request,slug):
    # return HttpResponse(f'this is blog post: {slug}')
    return render(request,'blog/blogpost.html')