from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.staffRegister, name='register'),
    path('login/', views.staffLogin, name='login'),
    path('logout/', views.staffLogout, name='logout'),
    path('complaint/', views.issue, name='complaint'),
    path('staff/', views.staff, name='staff'),
    path('contact/', views.contact, name='contact'),
]
