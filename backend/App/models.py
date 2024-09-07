from django.db import models

# Create your models here.
class info(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    
    def __str__(self):
        return f"{self.title}"


class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='project_images/')
    
    def __str__(self):
        return f"{self.title}"