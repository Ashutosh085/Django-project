# Generated by Django 5.0.2 on 2024-03-13 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_prouct_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pic',
            field=models.ImageField(null=True, upload_to='static/img/products/'),
        ),
    ]
