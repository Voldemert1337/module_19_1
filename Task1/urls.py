from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='products'),
    path('about/', views.about, name='about'),
    path('registration_page/', views.sign_up_by_django, name='registration_page'),

]

