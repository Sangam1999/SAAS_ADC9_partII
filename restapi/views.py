from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from WebApp.models import Book
import json

# Create your views here.
@csrf_exempt
def view_get_post_book(request):
    if request.method == 'GET':
        book_queryset = Book.objects.all()
        print(book_queryset)
        list_of_objects = list(book_queryset.values())
        print("list=>",list_of_objects)
        dict_name={
            "bookings":list_of_objects
        }

        return JsonResponse(dict_name)
    elif request.method == 'POST':
        print("Request body content =>",request.body)
        print("Request body type =>",type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python body contents =>",request.python_dictionary_object)
        print("Python body type =>",type(request.python_dictionary_object))
        Book.objects.create(name=python_dictionary_object['name'],email=python_dictionary_object['email'],phone=python_dictionary_object['phone'],number_of_adults=python_dictionary_object['number_of_adults'],number_of_children=python_dictionary_object['number_of_children'],arrival=python_dictionary_object['arrival'],checkOut=python_dictionary_object['checkOut'])
        return JsonResponse({
            "message":"Successfully posted"
        })
    else:
        return HttpResponse("Other http verbs testing")

@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    if request.method == 'GET':
        bookings=Book.objects.get(id=ID)
        return JsonResponse({
            "id":bookings.id,
            "name":bookings.name,
            "email":bookings.email,
            "phone":bookings.phone,
            "number_of_aduts":bookings.number_of_adults,
            "number_of_children":bookings.number_of_children,
            "arrival":bookings.arrival,
            "checkOut":bookings.checkOut
        })
    else:
        return JsonResponse({
            "message":"Other http verbs testings"
        })