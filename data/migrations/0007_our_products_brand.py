# Generated by Django 4.0 on 2022-01-01 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_remove_our_products_company_our_products_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='our_products',
            name='Brand',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
    ]