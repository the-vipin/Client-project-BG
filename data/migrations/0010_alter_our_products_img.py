# Generated by Django 4.0 on 2022-01-02 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_alter_our_products_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='our_products',
            name='img',
            field=models.ImageField(blank=True, default='background/default.jpg', upload_to='background/'),
        ),
    ]
