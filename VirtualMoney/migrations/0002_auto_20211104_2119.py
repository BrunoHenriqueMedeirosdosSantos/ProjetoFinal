# Generated by Django 3.2.8 on 2021-11-05 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VirtualMoney', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countrycurrencyuser',
            old_name='id_countrycurrency',
            new_name='countrycurrency',
        ),
        migrations.RenameField(
            model_name='countrycurrencyuser',
            old_name='id_user',
            new_name='user',
        ),
    ]