# Generated by Django 3.2.7 on 2021-11-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_market', '0013_rename_earnt_stockfolio_earned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockfolio',
            name='earned',
            field=models.FloatField(default=0, max_length=12),
        ),
        migrations.AlterField(
            model_name='stockfolio',
            name='net',
            field=models.FloatField(default=0, max_length=12),
        ),
        migrations.AlterField(
            model_name='stockfolio',
            name='spent',
            field=models.FloatField(default=0, max_length=12),
        ),
    ]