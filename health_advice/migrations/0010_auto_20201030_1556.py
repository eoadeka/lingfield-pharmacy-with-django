# Generated by Django 3.0.8 on 2020-10-30 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_advice', '0009_auto_20201030_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthadvice',
            old_name='category',
            new_name='categories',
        ),
    ]