# Generated by Django 4.0.2 on 2022-02-25 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Selling_price',
            new_name='selling_price',
        ),
    ]
