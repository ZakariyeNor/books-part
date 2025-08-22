from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)  # max_digits can be larger if needed
    inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} by {self.author}'
