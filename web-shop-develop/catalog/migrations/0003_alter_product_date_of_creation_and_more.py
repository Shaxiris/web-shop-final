# Generated by Django 4.2.4 on 2023-08-12 23:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_options_alter_product_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateField(default=datetime.date(2023, 8, 13), verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_last_change',
            field=models.DateField(default=datetime.date(2023, 8, 13), verbose_name='дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория'),
        ),
    ]
