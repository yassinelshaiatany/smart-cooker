from pages import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name="dashboard")
]
