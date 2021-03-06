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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    countrycurrency = models.ForeignKey(CountryCurrency, on_delete=models.CASCADE)
    def __str__(self):
        return f"Currency Users(User:{self.user}, Country Currency:{self.countrycurrency})"


class FavoriteCoins(models.Model):
    name = models.CharField(max_length=30)
    symbol = models.CharField(max_length = 5)
    