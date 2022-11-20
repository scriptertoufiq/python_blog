from django.urls import path
from App_blog import views

app_name = 'App_blog'
urlpatterns =[
    path('',views.BlogList.as_view(),name='index'),
    path('create_blog/',views.CreateBlog.as_view(),name='create_blog'),
    path('details/<slug:slug>',views.blog_detail,name='blog_detail'),
]