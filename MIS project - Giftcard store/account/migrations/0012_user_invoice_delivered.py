# Generated by Django 4.1.4 on 2022-12-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_invoice',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
