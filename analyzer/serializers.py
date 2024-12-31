from rest_framework import serializers

class ResumeAnalyzeSerializer(serializers.Serializer):
    resume = serializers.FileField()  # Accept file uploads
