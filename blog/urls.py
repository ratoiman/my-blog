from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.post_list, name='post_list'),
    path('cv', views.cv, name='cv'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]
