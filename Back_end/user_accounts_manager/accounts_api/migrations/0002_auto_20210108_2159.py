# Generated by Django 3.1.5 on 2021-01-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered_accounts',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
