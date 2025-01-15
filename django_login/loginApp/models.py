from django.db import models

class ProgrammingLanguage(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    frameworks = models.CharField(max_length=255, blank= True)  # Added field for frameworks
    founder = models.CharField(max_length=255, default="")  # Added field for founder

    def __str__(self):
        return self.name
