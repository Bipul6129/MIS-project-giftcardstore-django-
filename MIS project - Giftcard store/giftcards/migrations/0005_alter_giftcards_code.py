# Generated by Django 4.1.4 on 2022-12-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftcards', '0004_alter_giftcards_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcards',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
