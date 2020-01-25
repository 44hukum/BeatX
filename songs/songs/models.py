from django.db import models

class FileUpload(models.Model):
    uploadedBy=models.CharField(max_length=100)
    song=models.FileField(upload_to='uploaded/')
