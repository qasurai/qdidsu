# Generated by Django 3.2 on 2023-09-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0002_auto_20230928_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representative',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='studentnumber',
            field=models.IntegerField(unique=True),
        ),
    ]
