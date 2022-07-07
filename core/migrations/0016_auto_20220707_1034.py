# Generated by Django 3.0.5 on 2022-07-07 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20220621_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, choices=[('L', 'Laptops'), ('P', 'Phones'), ('W', 'Watches'), ('A', 'Accessories')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(blank=True, choices=[('B', 'BestSeller'), ('N', 'New'), ('D', 'Discount'), ('P', 'Promotion')], max_length=2, null=True),
        ),
    ]
