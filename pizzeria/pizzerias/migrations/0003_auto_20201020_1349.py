# Generated by Django 3.1.2 on 2020-10-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzerias', '0002_toppings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toppings',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]