# Generated by Django 4.0 on 2022-01-01 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_our_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='our_products',
            name='company',
        ),
        migrations.AddField(
            model_name='our_products',
            name='Company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data.our_business'),
        ),
    ]
