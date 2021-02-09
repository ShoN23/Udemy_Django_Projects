from django.shortcuts import render
from .models import User
# Create your views here.


def user(request):
    user_dic = {'users': User.objects.all()}
    return render(request, 'user.html', context=user_dic)

