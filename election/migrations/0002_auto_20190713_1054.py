# Generated by Django 2.1 on 2019-07-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='post',
            field=models.CharField(max_length=50),
        ),
    ]
