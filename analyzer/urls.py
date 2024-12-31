from django.urls import path
from .views import classify_resume

urlpatterns = [
    path('classify-resume/', classify_resume, name='classify_resume'),
]
