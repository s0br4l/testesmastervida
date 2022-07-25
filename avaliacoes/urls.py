from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('userlist', views.userlist, name='userlist'),
    path('users/<user_id>', views.users, name='users'),
    path('newuser', views.newuser, name='newuser'),
    path('antropometria/<user_id>', views.antropometria, name='antropometria'),
    path('testes/<user_id>', views.testes, name='testes'),
    path('dexa/<user_id>', views.dexa, name='dexa'),

    ]
