# Generated by Django 2.2.14 on 2022-10-24 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodtests', '0004_auto_20221024_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='code',
            field=models.CharField(max_length=4),
        ),
    ]
