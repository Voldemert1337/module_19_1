from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Buyer(models.Model):
    #username
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    age = models.IntegerField(validators=[MaxValueValidator(120)])

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    size = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField('Buyer', related_name='games')

    def __str__(self):
        return self