from django.urls import path
from . import views

urlpatterns = [
    path('your-endpoint/', views.your_view, name='your-view'),
]
