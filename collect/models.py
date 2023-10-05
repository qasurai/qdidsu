from django.db import models

# Create your models here.

college_u=(
    ('L','Lyceum'),
    ('P','Parnassus'),
    ('V','Virtus'),
)
grade_u=(
    ('9','G9'),
    ('10','G10'),
    ('11','G11'),
    ('12','G12'),
)
mentor_u=(
    ('A','郭俊卿'),
    ('B','赵胡梦鹤'),
    ('C','刘芳雨'),
    ('D','王倩宇'),
    ('E','赵航'),
    ('F','高行健'),
    ('G','王思洋'),
    ('H','朱宝杰'),
    ('I','周芳颖'),
    ('J','孙莹莹'),
    ('K','赵昊一'),
    ('L','李帅'),
    ('M','兰文稚'),
    ('O','王一童'),
    ('P','李肖阳'),
    ('Q','于晓冬'),
    ('R','苏盼文'),
    ('S','王菁'),
    ('T','李妍'),
    ('U','邢文娟'),
    ('V','王乃伟'),
    ('W','徐颖雪'),
    ('X','于江'),
    ('Y','林帅'),
)

class Representative(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,unique=True)
    college=models.CharField(max_length=1,choices=college_u)
    grade=models.CharField(max_length=2,choices=grade_u)
    mentor=models.CharField(max_length=1,choices=mentor_u)
    studentnumber=models.IntegerField(unique=True)
    content=models.TextField(default="")
    create_data=models.DateTimeField(auto_now_add=True)
    last_change_data=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name