from django.urls import path
from .import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('login/',views.login_user,name='login'),
    path('mygiftcards/',views.mygiftcards,name='mygiftcards')

]