# Generated by Django 2.2.14 on 2022-10-24 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodtests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='lower',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='upper',
            field=models.FloatField(blank=True, null=True),
        ),
    ]