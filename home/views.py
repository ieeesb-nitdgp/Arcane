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



    # p = get_object_or_404(Leaders, pk=1)
    # n = p.playerNum
    # lst = [0, 1, 2]
    # form = UserAnswer

    # if request.method == 'GET':
    #     # print(n)
    #     j = 1
    #     leaders = Player.objects.order_by(
    #         '-score', 'last_submit')[:n]

    #     email_list = []

    #     for i in leaders:
    #         i.rank = j
    #         j += 1
    #         i.save()

    #         email_list.append(i.email)

    #     print(email_list)
    #     return render(request, 'home/page.html', {"n": n, "leaders": leaders, "form": form, "lst": lst[0]})

    # if request.method == "POST":    # if the admin submits the passcode
    #     my_form = UserAnswer(request.POST)

    #     if my_form.is_valid():
    #         ans = my_form.cleaned_data.get("answer")
    #         organs = "AlohaMoraHarryPotter"

    #         # shit code below 

    #         # correct answer
    #         if (str(organs) == str(ans)):   # if the answer is correct
    #             leaders = Player.objects.order_by(
    #                 '-score', 'last_submit')[:n]
                
    #             u = 

    #             Player.objects.filter( score > u ).update(name="foo")


    #             for x in leaders:
    #                 x.level2 = 0           
                    
    #                 x.save()
    #                 print(x.name)

    #                 with open('text_messages/login_user.txt', 'r') as file:
    #                     data_email = file.read()

    #                 send_mail(
    #                         'Congrats, you cleared round 1 !',
    #                         str(data_email).format(x.name),
    #                         'ieeesbnitd@gmail.com',
    #                         [x.email],
    #                         fail_silently=True,
    #                         )



    #             return render(request, 'home/page.html', {"n": n, "leaders": leaders, "form": form, "lst": lst[1]})

    #         # incorrect answer
    #         else:   # returns the same page
    #             leaders = Player.objects.order_by(
    #                 '-score', 'last_submit')[:n]
    #             return render(request, 'home/page.html', {"n": n, "leaders": leaders, "form": form, "lst": lst[2]})
    #     else:
    #         return HttpResponse('<h2> Your Form Data was Invalid </h2>')






