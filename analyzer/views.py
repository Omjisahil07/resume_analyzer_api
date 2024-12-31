from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pickle
import os
from rest_framework.decorators import api_view
from django.conf import settings
import pandas as pd
from .models import Resume

class ResumeAnalyzerAPIView(APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('resume')
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Load the model
        with open('resumeclassifier.pkl', 'rb') as model_file:
            model = pickle.load(model_file)

        # Example processing logic
        response_data = {"message": "File processed successfully"}
        return Response(response_data, status=status.HTTP_200_OK)
# analyzer/views.py
from django.http import JsonResponse

def your_view(request):
    data = {"message": "Hello, world!"}
    return JsonResponse(data)

# Load the pickle file
model_path = os.path.join(settings.BASE_DIR, 'analyzer', 'ml_models', 'resume_classifier.pkl')
with open(model_path, 'rb') as file:
    clf_model = pickle.load(file)

@api_view(['POST'])
def classify_resume(request):
    try:
        if 'resume' not in request.FILES:
            return Response({'error': 'No resume file provided'}, 
                          status=status.HTTP_400_BAD_REQUEST)

        resume_file = request.FILES['resume']
        
        # Save the resume
        resume = Resume.objects.create(file=resume_file)
        
        # Extract text from resume (you'll need to implement this based on file type)
        resume_text = extract_text_from_resume(resume_file)
        
        # Preprocess the text (implement this based on your model requirements)
        processed_text = preprocess_text(resume_text)
        
        # Make prediction
        prediction = clf_model.predict([processed_text])[0]
        
        # Update the resume category
        resume.predicted_category = prediction
        resume.save()
        
        return Response({
            'category': prediction,
            'confidence': float(clf_model.predict_proba([processed_text]).max()),
            'resume_id': resume.id
        })
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def extract_text_from_resume(file):
    # Implement text extraction based on file type (PDF, DOCX, etc.)
    # You might want to use libraries like PyPDF2, python-docx, etc.
    pass

def preprocess_text(text):
    # Implement text preprocessing similar to what was used during model training
    # This might include:
    # - Converting to lowercase
    # - Removing special characters
    # - Tokenization
    # - Removing stop words
    # - etc.
    pass
