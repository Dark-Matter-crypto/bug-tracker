# Generated by Django 3.1.4 on 2020-12-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20201218_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ticketattachment',
            name='note',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='todo',
            name='note',
            field=models.CharField(max_length=50),
        ),
    ]