# Generated by Django 4.0 on 2021-12-29 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_staff',
        ),
    ]
