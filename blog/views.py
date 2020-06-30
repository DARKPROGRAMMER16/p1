from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,BlogComment
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.

def bloghome(request):
    allpost = Post.objects.all()[::-1]
    context = {'allpost':allpost}
    return render(request,'blog/bloghome.html',context)

def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    repdict = {}
    for reply in replies:
        if reply.parent.sno not in repdict.keys():
            repdict[reply.parent.sno]=[reply]
        else:
            repdict[reply.parent.sno].append(reply)
    print(repdict)
    context = {'post':post,'comments':comments,'user':request.user,'repdict':repdict}
    return render(request,'blog/blogpost.html',context)

def postComment(request):
    if request.method=="POST": 
        comment = request.POST.get("comment")
        user = request.user
        postsno = request.POST.get("postsno")
        post = Post.objects.get(sno=postsno)
        parentSno = request.POST.get("parentSno")
        if parentSno=="":
            comment = BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,"your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request,"your reply has been posted successfully")
            
    return redirect(f"/blog/{post.slug}")