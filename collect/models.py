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
    content=models.TextField(default="",null=True,blank=True)
    create_data=models.DateTimeField(auto_now_add=True)
    last_change_data=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Proposal(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.CharField(max_length=50,unique=True,null=True,blank=True)
    init_views=models.BooleanField(null=True)
    init_opinion=models.TextField(default="",null=True,blank=True)
    forrep=models.ForeignKey('Representative',on_delete=models.CASCADE,related_name='forrep')
    forrep_1=models.ForeignKey('Representative',on_delete=models.CASCADE,null=True,blank=True,related_name='forrep_1')
    forrep_2=models.ForeignKey('Representative',on_delete=models.CASCADE,null=True,blank=True,related_name='forrep_2')
    forrep_3=models.ForeignKey('Representative',on_delete=models.CASCADE,null=True,blank=True,related_name='forrep_3')
    title=models.CharField(max_length=50)
    reason=models.TextField(default="",null=True,blank=True)
    solvetion=models.TextField(default="",null=True,blank=True)
    result=models.BooleanField(null=True)
    create_data=models.DateTimeField(auto_now_add=True)
    last_change_data=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.title
    
class News(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,unique=True)
    content=models.TextField(default="",null=True,blank=True)
    create_data=models.DateTimeField()
    class Meta:
        ordering = ['-create_data']
        verbose_name='News'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title