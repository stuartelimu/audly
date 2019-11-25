from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=100)
    upload = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title