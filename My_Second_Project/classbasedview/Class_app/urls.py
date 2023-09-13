from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from Class_app import views

app_name = 'class_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name="viewindex" ),
    path('detailsview/<pk>/', views.MoreInfo.as_view(), name='details'),
    path('add_person/', views.AddPerson.as_view(), name='add_person'),
    path('update_person/<pk>/', views.UpdatePerson.as_view(), name='add_person'),
    path('delete_person/<pk>/', views.DeletePerson.as_view(), name='delete_person'),
]