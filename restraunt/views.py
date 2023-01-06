from django.shortcuts import render,HttpResponse
from django.http import HttpResponse,HttpRequest
from restraunt.models import Booking,Message
from datetime import datetime
# Create your views here.
def rangrez(request):
     return render(request,"index.html")


    
def requestfillform(request:HttpRequest):
    if request.method == 'POST':
        return HttpResponse(save_message(request.POST.dict()))
    print('2 Called')  

    return HttpResponse("ok json")


def bookTable(request:HttpRequest):
    if request.method == 'POST':
        return HttpResponse(book_table(request.POST.dict()))
#helpers

class Returns:
    Sucess = "Thank You Connecting With Us !"
    Error = "Could Not Complete Action !"
    Resp = "OK"


def book_table(obj:dict):
    print(obj)
    try:
        booking = Booking()
        booking.name = obj['name']
        booking.members = int(obj['people'])
        booking.time = obj['time']
        booking.message = obj['message']
        booking.date = datetime.strptime(str(obj["date"]),"%Y-%m-%d")
        booking.email = obj['email']
        booking.phone = obj['phone']
        booking.save()
        return Returns.Resp
    except Exception as e:
        print("Booking Error : ",e)
        return Returns.Error


def save_message(obj:dict):
    print(obj)
    try:
        m = Message()
        m.name = str(obj['name'])
        m.email = obj['email']
        m.subject = obj['subject']
        m.body = obj['message']
        m.save()
        return Returns.Resp
    except Exception as e:
        print(e)
        return Returns.Error