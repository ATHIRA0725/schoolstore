# Generated by Django 4.2 on 2023-04-05 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('cpassword', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]
