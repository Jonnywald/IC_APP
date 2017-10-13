from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,Users

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request,'first_app/index.html',context=date_dict)
def help(request):
    help_dict = {'help_insert':'HELP!'}
    return render(request,'first_app/help.html',context=help_dict)
def user(request):
    user_list = Users.objects.order_by('email')
    user_dict = {'users_key' : user_list}
    return render(request,'first_app/user.html',context=user_dict)
def reta(request):
    return render(request,'first_app/reta.html')
def parabola(request):
    return render(request,'first_app/parabola.html')
def circulo(request):
    return render(request,'first_app/circulo.html')
def elipse(request):
    return render(request,'first_app/elipse.html')
def hiperbole(request):
    return render(request,'first_app/hiperbole.html')
def outros(request):
    return render(request,'first_app/outros.html')
def trigonometria(request):
    return render(request,'first_app/trigonometria.html')
