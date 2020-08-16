from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.post_list, name='post_list'),
    path('contact', views.contact, name='contact'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]
