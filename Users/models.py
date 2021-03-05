from django.db import models

# Create your models here.
    
class Skills(models.Model):
    skills_set = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Skills
    
class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    skills_set = models.ForeignKey(Skills, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
