"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
import blog.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
   path('blog/',blog.views.allblog,name='blog'),
   path('blog/<int:blog_id>',blog.views.details, name='detail'),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('create/',views.create,name="create"),
    path('update/<int:blog_id>',views.update,name="update"),
    path('remove/<int:blog_id>',views.remove,name="remove"),
    path('logout/',views.logout,name='logout'),
    path('vote/<int:blog_id>',views.vote,name='vote'),
    path('base/',views.base,name='base')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#for location
