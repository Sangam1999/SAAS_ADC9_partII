from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from .models import Book
# Create your views here.

def home(request):
    return render(request,'booking.html')

def data_save(request):
    get_name=request.POST.get("name")
    get_email=request.POST.get("email")
    get_phone=request.POST.get("phone")
    get_number_of_adults=request.POST.get("number_of_adults")
    get_number_of_children=request.POST.get("number_of_children")
    get_arrival=request.POST.get("arrival")
    get_checkOut=request.POST.get("checkOut")
    get_payment=request.POST.get("payment")
    get_comment=request.POST.get("comment")

    book_obj= Book(name=get_name,email=get_email,phone=get_phone,number_of_adults=get_number_of_adults,number_of_children=get_number_of_children,arrival=get_arrival,checkOut=get_checkOut,payment=get_payment,comment=get_comment)
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
    book_obj.payment=request.POST['payment']
    book_obj.comment=request.POST['comment']
    book_obj.save()

    return HttpResponse("Record Updated Successfully!!")

def delete_object(request,ID):
    obj= Book.objects.get(id=ID)
    obj.delete()

    return HttpResponse("Record delete Successfully!!")



    