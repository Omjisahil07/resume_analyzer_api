from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pickle

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
