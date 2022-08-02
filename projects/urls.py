from django.urls import path
from .views import index, portfolio_details

urlpatterns = [
    path('', index, name='home'),
    path('project-details/<int:pk>/', portfolio_details, name='project-details'),
]