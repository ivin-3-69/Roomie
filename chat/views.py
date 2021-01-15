from django.shortcuts import render
from .models import chatdb
from django.http import HttpResponse


def index(request):

    user_list = chatdb.objects.all()
    context = {
        'user_list': user_list,
        }
    return render(request, 'chat/index.html',context)

def personal(request, user_id):

    return HttpResponse("you are viewing the chat of user %s" %user_id)
