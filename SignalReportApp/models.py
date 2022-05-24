from djongo import models

# Create your models here.

class SignalReport(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    body = models.CharField(max_length=1000, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)