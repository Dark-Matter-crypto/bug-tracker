# Generated by Django 3.1.4 on 2021-01-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0020_auto_20210105_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directmessage',
            name='body',
            field=models.CharField(max_length=500),
        ),
    ]