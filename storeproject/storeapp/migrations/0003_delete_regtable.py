# Generated by Django 4.2 on 2023-04-05 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_regtable_delete_store'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Regtable',
        ),
    ]