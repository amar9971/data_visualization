from django.db import models

# Create your models here.
class Countrydata(models.Model):
    country = models.CharField(max_length=100)
    intensity = models.IntegerField()
    sector=models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural="country intensity data"
    
    def __str__(self):
        return f'{self.country}-{self.intensity}-{self.sector}'