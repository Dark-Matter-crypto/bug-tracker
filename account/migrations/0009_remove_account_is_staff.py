# Generated by Django 3.1.4 on 2020-12-31 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20201230_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_staff',
        ),
    ]