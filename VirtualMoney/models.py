from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=60)
    def __str__(self):
        return f"User(Name:{self.name}, Username:{self.username}, Email:{self.email})"

class Country(models.Model):
    country = models.CharField(max_length=40)
    def __str__(self):
        return f"Country(Country:{self.country})"

class CountryCurrency(models.Model):
    currency = models.CharField(max_length=3)
    def __str__(self):
        return f"CountryCurrency(Currency:{self.currency})"

class CountryCurrencyUser(models.Model):
    id_user = models.IntegerField()
    id_countrycurrency = models.IntegerField()