from django.db import models
from datetime import datetime


class currencydata(models.Model):

    country_name = models.CharField(max_length = 120)
    country_code = models.CharField(max_length=5)
    country_currency_value = models.DecimalField(max_digits=25, decimal_places=20)
    currency_update_time = models.DateTimeField(default=datetime.now, blank=True)