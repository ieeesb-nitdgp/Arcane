from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Leaders
from user.models import Player
from quiz.forms import UserAnswer
from django.core.mail import send_mail
from django.contrib import messages

from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
@staff_member_required
def email_users(request) :
    player = Player.objects.all()
    return render(request, 'home/emails.html', {'players':player})


def not_logged_in(user):
    return not user.is_authenticated


def base(request):
    return render(request, 'home/base.html')


def home(request):
    return render(request, 'home/home.html')


def hello(request):
    return render(request, 'home/hello.html')


def rules(request):
    return render(request, 'home/rule.html')


def error_404(request, exception):
        data = {}
        return render(request,'home/404.html', data)


@staff_member_required
def page(request):
    "Only After 1st Round is complete"

    '''rewrite this functtion it work shit 
    https://sayanmondal.tech/blog/jekyll/update/2021/12/16/DjangoBulkUpdate.html
    '''

    return HttpResponse("Build in progress")






