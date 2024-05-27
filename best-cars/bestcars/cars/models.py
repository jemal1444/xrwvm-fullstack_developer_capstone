from django.db import models
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

