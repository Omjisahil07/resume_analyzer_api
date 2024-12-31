from django.db import models

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    predicted_category = models.CharField(max_length=100, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume {self.id} - {self.predicted_category}"
