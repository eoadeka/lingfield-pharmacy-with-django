# Generated by Django 3.1.1 on 2020-12-14 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20201209_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shipping_cost',
            field=models.CharField(default='1', max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='total_excl_vat',
            field=models.FloatField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='vat',
            field=models.FloatField(default='1'),
            preserve_default=False,
        ),
    ]