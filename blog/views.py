from django.shortcuts import render,HttpResponse

# Create your views here.
def bloghome(request):
    return HttpResponse('this is blog home')
def blogpost(request,slug):
    return HttpResponse(f'this is blog post: {slug}')