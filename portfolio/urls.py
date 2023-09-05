from django.urls import path
from portfolio.views import home,logout_user,signin,signup,userdetails,projectdetails,createproject,deleteproject,profil
urlpatterns = [
    path('',home,name='home'),
    path('logout',logout_user,name='logout'),
    path('signin',signin,name='signin'),
    path('signup',signup,name='signup'),
    path('userdetails/<int:pk>',userdetails,name='userdetails'),
    path('projectdetails/<int:pk>',projectdetails,name='projectdetails'),
    path('createproject',createproject,name='createproject'),
    path('<int:project_id>/delete/', deleteproject, name='deleteproject'),
    path('profil',profil,name='profil'),

]