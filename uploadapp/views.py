from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage

from .models import profile

# Create your views here.
def index(request):
    all_uploads =profile.objects.all()
    return render(request,'home.html',{'uploads':all_uploads})

def normalupload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        url=fs.url(filename)
        new_profile=profile(image=url)
        new_profile.save()
        redirect('home/')
    else:
        return  redirect('home/')