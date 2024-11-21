from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.download_pdfs, name='download_pdfs'),
    path('index1/', views.esign, name='esign'),
    path('index2/', views.before2018, name='before2018')
]
