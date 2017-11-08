from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Users
from first_app import forms
from first_app.forms import NewUser

# Create your views here.
def index(request):
    return render(request,'first_app/index.html')
def help(request):
    help_dict = {'help_insert':'HELP!'}
    return render(request,'first_app/help.html',context=help_dict)
def user(request):
    form = NewUser()
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'first_app/user.html',{"form":form})
def reta(request):
    CoefLinT1 = forms.TesteSimples()
    CoefAngT1 = forms.TesteSimples()
    return render(request,'first_app/reta.html',{'test1':CoefLinT1,'test2':CoefAngT1})
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
def form_name_view(request):
    form = forms.NewUser()
    return render(request,'first_app/form_page.html',{'form':form})
