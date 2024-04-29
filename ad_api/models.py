from django.db import models
    

class Ad(models.Model):
    ad_type = models.CharField(max_length=10)
    date = models.DateField()
    ads_run = models.IntegerField()
    spend = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.ad_type} - {self.date}"
