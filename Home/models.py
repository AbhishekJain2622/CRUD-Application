from django.db import models

# Create your models here.
class Entry(models.Model):
    ID = models.IntegerField(primary_key=True)
    data1 = models.CharField(max_length=50)
    data2 = models.CharField(max_length=50)
