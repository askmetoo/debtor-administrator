# Generated by Django 2.1.3 on 2019-08-07 18:28

import backend.api.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190807_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debtor',
            name='iban',
            field=backend.api.models.IBANField(include_countries=None, max_length=34, use_nordea_extensions=False),
        ),
    ]