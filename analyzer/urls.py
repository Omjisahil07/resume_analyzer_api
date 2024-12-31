from django.urls import path
from .views import ResumeAnalyzerAPIView

urlpatterns = [
    path('analyze/', ResumeAnalyzerAPIView.as_view(), name='analyze-resume'),
]
