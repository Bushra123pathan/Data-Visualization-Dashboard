from django.db import models

class SalesData(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=100)
    sales_amount = models.FloatField()

    def __str__(self):
        return f"{self.category} - {self.sales_amount}"
