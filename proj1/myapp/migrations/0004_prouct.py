# Generated by Django 5.0.2 on 2024-03-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prouct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]