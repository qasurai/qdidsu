# Generated by Django 2.1 on 2023-09-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0003_auto_20230928_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='representative',
            name='content',
            field=models.TextField(default=''),
        ),
    ]