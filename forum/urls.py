from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_lista, name='forum_lista'),
    path('topico/', views.forum_detalhe, name='forum_detalhe'),
]