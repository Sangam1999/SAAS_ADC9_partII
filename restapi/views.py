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
        return HttpResponse("POST testing")
    else:
        return HttpResponse("Other http verbs testing")