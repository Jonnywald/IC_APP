from django.conf.urls import url
from first_app import views

app_name = 'first_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^help/$', views.help,name='help'),
    url(r'^users/$', views.user,name='user'),
    url(r'^reta/$', views.reta,name='reta'),
    url(r'^parabola/$', views.parabola,name='parabola'),
    url(r'^circulo/$', views.circulo,name='circulo'),
    url(r'^elipse/$', views.elipse,name='elipse'),
    url(r'^hiperbole/$', views.hiperbole,name='hiperbole'),
    url(r'^outros/$', views.outros,name='outros'),
    url(r'^trigonometria/$', views.trigonometria,name='trigonometria'),
    url(r'^formpage/$',views.form_name_view,name='form_page'),
]
