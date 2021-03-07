from django.db import models

# Create your models here.
    
class Skills(models.Model):
    skills= models.CharField(max_length=100)
    
    def __str__(self):
        return self.skills
    
class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    skillt = models.ForeignKey(Skills, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
