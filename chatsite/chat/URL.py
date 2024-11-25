from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a página inicial do chat
    path('about/', views.about, name='sobre'),
    path('contact/', views.contact, name='contatos'),
    path('register/', views.register, name='cadastro'),
    path('success/', views.success, name='cadastro_sucesso'),
]
