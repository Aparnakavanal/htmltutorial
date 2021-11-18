from django.urls import path
from .views import *

urlpatterns = [
    path("home",Home,name="home"),
    path("pageone",pone,name="one"),
    path("pagetwo",ptwo,name="two"),
    path("pagethree",pthree,name="three"),
    path("pagefour",pfour,name="four")

]