from django.shortcuts import render
from .models import chatdb
from django.http import HttpResponse

def index(request,order):
    if order == "desc":
        user_list = chatdb.objects.order_by('-time_match')
    elif order == "asc":
        user_list = chatdb.objects.order_by('time_match')
    context = {
        'user_list': user_list,
        'order': order,
        }
    return render(request, 'chat/index.html',context)

def personal(request, user_id):

    return HttpResponse("you are viewing the chat of user %s" %user_id)