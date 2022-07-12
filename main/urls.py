from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('questions/<str:subj>', views.viewQuestions, name='questions'),
    path('login/', views.viewLogin, name='login'),
    # path('home/', views.vLogin, name='login')
]

