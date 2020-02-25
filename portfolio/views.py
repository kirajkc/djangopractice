from django.shortcuts import render
from job.models import job
from django.shortcuts import get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.models import blog


def home(request):
    jobs = job.objects
   
    return render(request,'home.html',{'job':jobs})
def signup(request):
    if request.method == 'POST':
        #user has info and wants an account now
        if request.POST['password1']== request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'signup.html',{'error':'user already exist'})
            except:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return render(request,'blog.html')
        else:
            return render(request,'signup.html',{'error':"password did not match"})
        
    return render(request,'signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'],password=request.POST['password1'])
        if user is not None:
            auth.login(request,user)
            return redirect('blog')
        else:
            return render(request,'login.html',{'error':"username or password is incorrect"})
    else:
            return render(request,'login.html')
    return render(request,'login.html')
@login_required(login_url="login/")
def create(request):
    if request.method=="POST":
        if request.FILES['image'] and request.POST['summary']:
            j=blog()
            j.image=request.FILES['image']
            j.summary=request.POST['summary']
            j.time=request.POST['time']
            j.title=request.POST['title']
            j.user=request.user
            j.save()
            return redirect('blog')
        else:
            return render(request,'create.html',{'error':"no product found"})
    return render(request,'create.html')
@login_required(login_url="login/")
def update(request,blog_id):
    d=get_object_or_404(blog,pk=blog_id)
    if request.method=="POST":
        if request.FILES['image'] and request.POST['summary']:
            d.image=request.FILES['image']
            d.summary=request.POST['summary']
            d.time=request.POST['time']
            d.title=request.POST['title']
            d.save()
            return redirect('blog')
        else:
            return render(request,'update.html',{'error':"no product found"})
    return render(request,'update.html',{'update':d})
@login_required(login_url="login/")
def remove(request,blog_id):
    d=get_object_or_404(blog,pk=blog_id)
    d.delete()
    return redirect('blog')
    
def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return redirect('blog')
    return render(request,'blog.html')
@login_required(login_url="login/")  
def vote(request,blog_id):
    d=get_object_or_404(blog,pk=blog_id)
    if request.method=='POST':
        d.vote=d.vote+1
        d.save()
        return redirect('blog')
    return render(request,'blog.html')
    
def base(request):
    return render(request,'base.html')

