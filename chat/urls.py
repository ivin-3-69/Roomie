from django.urls import path

from . import views

urlpatterns = [
   path('home/', views.index, name='index'),
   path('<int:user_id>/', views.personal, name='personal_chat'),
]