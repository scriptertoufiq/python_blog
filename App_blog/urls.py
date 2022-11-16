from django.urls import path
from App_blog import views

app_name = 'App_blog'
urlpatterns =[
    path('',views.index,name='index'),
]