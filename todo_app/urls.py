from django.urls import path

from todo_app import views

urlpatterns = [
    path('',views.test,name="test"),
    path('home',views.home,name="home"),
    path('index',views.index,name="index"),
    path('indexx',views.indexx,name="indexx"),

]