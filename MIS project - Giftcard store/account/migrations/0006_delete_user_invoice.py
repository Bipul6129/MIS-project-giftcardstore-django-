# Generated by Django 4.1.4 on 2022-12-19 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_invoice_invoice'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_invoice',
        ),
    ]
