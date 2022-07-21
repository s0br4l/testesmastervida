from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('userlist', views.userlist, name='userlist'),
    path('antropometria/<n_user>', views.antropometria, name='antropometria'),
    path('testes/<n_user>', views.testes, name='testes'),
    path('dexa/<n_user>', views.dexa, name='dexa'),

    ]
