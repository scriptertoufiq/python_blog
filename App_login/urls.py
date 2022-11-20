from django.urls import path
from App_login import views

app_name = 'App_login'


urlpatterns =[
    path('signup/',views.signUp,name='signup'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.user_profile,name='profile'),
    path('change/profile/',views.user_profile_change,name='change_profile'),
    path('change/password/',views.pass_change,name='pass_change'),
    path('add/profile/picture/',views.add_pro_pic,name='add_pro_pic'),
    path('update/profile/picture/',views.change_pro_pic,name='change_pro_pic'),
]

