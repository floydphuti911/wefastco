# Generated by Django 3.1 on 2022-05-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220521_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]