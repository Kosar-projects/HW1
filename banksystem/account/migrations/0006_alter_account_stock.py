# Generated by Django 4.2 on 2024-08-11 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_account_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='stock',
            field=models.BigIntegerField(),
        ),
    ]
