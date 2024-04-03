from django.db import models

# Create your models here.

#models
#makes
class Make(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Autos(models.Model):
    nickname = models.CharField(max_length = 100)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    mileage = models.IntegerField()
    comments = models.TextField()


