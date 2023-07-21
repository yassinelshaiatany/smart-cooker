from accounts import views
from django.urls import path

urlpatterns = [
    path('', views.verify_options, name='verify_options'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout')
]