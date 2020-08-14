from django.db import models

# Create your models here.
class food_list(models.Model):
    name = models.CharField(max_length=40,primary_key=True)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    storage_type = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    expiry_date = models.DateField()

#    def __str__(self):
#        return self.name+' expires:'+ self.expiry_date
