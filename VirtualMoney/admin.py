from django.contrib import admin

from VirtualMoney.models import Country, CountryCurrency, CountryCurrencyUser, User

# Register your models here.

admin.site.register(User)
admin.site.register(Country)
admin.site.register(CountryCurrency)
admin.site.register(CountryCurrencyUser)