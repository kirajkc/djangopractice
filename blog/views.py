from django.shortcuts import render,get_object_or_404
from blog.models import blog

def allblog(request):
    b=blog.objects
    return render(request,'blog.html',{'blog':b})
def details(request,blog_id):
    d=get_object_or_404(blog,pk=blog_id)
    return render(request,'detail.html',{'detail':d})
# Create your views here.
