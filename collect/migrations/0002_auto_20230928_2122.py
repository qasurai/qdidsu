# Generated by Django 3.2 on 2023-09-28 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='representative',
            name='studentnumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='representative',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='representative',
            name='mentor',
            field=models.CharField(choices=[('A', '郭俊卿'), ('B', '赵胡梦鹤'), ('C', '刘芳雨'), ('D', '王倩宇'), ('E', '赵航'), ('F', '高行健'), ('G', '王思洋'), ('H', '朱宝杰'), ('I', '周芳颖'), ('J', '孙莹莹'), ('K', '赵昊一'), ('L', '李帅'), ('M', '兰文稚'), ('O', '王一童'), ('P', '李肖阳'), ('Q', '于晓冬'), ('R', '苏盼文'), ('S', '王菁'), ('T', '李妍'), ('U', '邢文娟'), ('V', '王乃伟'), ('W', '徐颖雪'), ('X', '于江'), ('Y', '林帅')], max_length=1),
        ),
    ]