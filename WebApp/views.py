from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from .models import Book
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def view_hello_world(request):
    print(request.user)
    if request.user.is_authenticated:
        return HttpResponse("Hello Qorl")
    else:
        return HttpResponse("Error")

def home(request):
    return render(request,'booking.html')

def upload(request):
    context={}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request,'booking.html', context)

def data_save(request):
    get_name=request.POST.get("name")
    get_email=request.POST.get("email")
    get_phone=request.POST.get("phone")
    get_number_of_adults=request.POST.get("number_of_adults")
    get_number_of_children=request.POST.get("number_of_children")
    get_arrival=request.POST.get("arrival")
    get_checkOut=request.POST.get("checkOut")

    book_obj= Book(name=get_name,email=get_email,phone=get_phone,number_of_adults=get_number_of_adults,number_of_children=get_number_of_children,arrival=get_arrival,checkOut=get_checkOut)
    book_obj.save()

    return render(request,'booking.html')


def table(request):
    data=Book.objects.all()
    search=request.GET.get('search')

    if search !='' and search is not None:
        data=data.filter(name__icontains=search)
    context = {
        'Info':data
    }
    return render(request,'admin.html',context)


def view_update_booking(request,ID):
    book_obj=Book.objects.get(id=ID)
    context_variable={
        'book':book_obj
    }
    return render(request,'bookingupdate.html',context_variable)

def  view_update_form_data_in_db(request,ID):
    book_obj=Book.objects.get(id=ID)

    book_obj.name=request.POST['name']
    book_obj.email=request.POST['email']
    book_obj.phone=request.POST['phone']
    book_obj.number_of_adults=request.POST['number_of_adults']
    book_obj.number_of_children=request.POST['number_of_children']
    book_obj.arrival=request.POST['arrival']
    book_obj.checkOut=request.POST['checkOut']
    book_obj.save()

    return HttpResponse("Record Updated Successfully!!")

def delete_object(request,ID):
    obj= Book.objects.get(id=ID)
    obj.delete()

    return HttpResponse("Record delete Successfully!!")

def view_register_user(request):
    if request.method =="GET":
        return render(request,'registration/register.html')
    else:
        print(request.POST)
        user = User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()
        return HttpResponse("Sign up Successful")

def view_authenticate_user(request):
    if request.method=="GET":
        return render(request,'registration/login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['input_username'],password=request.POST['input_password'])
        print(user)
        if user is not None:
            login(request,user)
            return render(request,"welcome.html")
        else:
            return HttpResponse('Authentication Failed')

