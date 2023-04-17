from django.db import models


# Create your models here.

class Title(models.Model):
    name = models.CharField(max_length=50)
    total = models.FloatField()
    

class Depense(models.Model):
    title = models.CharField(max_length=50)
    montant = models.FloatField()
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    
    
    def __str__(self):
        return self.title
    
