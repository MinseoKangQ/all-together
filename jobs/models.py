from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.

User = get_user_model()

class Class (models.Model):
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE)
    name = models.TextField(verbose_name='이름') 
    image = models.ImageField(verbose_name = '프로필') 
    gender = models.TextField(verbose_name='성별') 
    age = models.IntegerField(verbose_name='나이') 
    school = models.TextField(verbose_name='학력') 
    cost = models.IntegerField(verbose_name='수업비용', default=10000) 
    times =models.TextField(verbose_name='시간대', null=True, blank=True) 
    info = models.TextField(verbose_name='강사정보',null=True, blank=True ) 
    student = models.TextField(verbose_name='수업 대상',null=True, blank=True) 
    feature = models.TextField(verbose_name='특이사항', null=True, blank=True) 
    group = models.TextField(verbose_name='수업분류', null=True, blank=True) 
    nationality = models.TextField(verbose_name='국적',null=True, blank=True)
    language = models.TextField(verbose_name='언어',null=True, blank=True)
    account = models.IntegerField(verbose_name='계좌번호', default=0,null=True, blank=True) 
    scrap = models.ManyToManyField(User, related_name='스크랩',blank = True)
    created_at = models.DateTimeField(verbose_name = '작성일',default=timezone.now)
    # 지불방식
    
    
class Register(models.Model):
    class_name = models.ForeignKey(to = 'Class', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE,null=True, blank=True)
    student_name = models.TextField(verbose_name='이름') 
    student_age = models.IntegerField(verbose_name='나이')
    student_phone = models.CharField(verbose_name='전화번호',max_length=50)
    student_image = models.ImageField(verbose_name='프로필',null=True,blank = True)
    student_email = models.TextField(verbose_name='이메일')
    pay = models.TextField(verbose_name='지불방식')
    times =models.TextField(verbose_name='시간대', null=True, blank=True) 
    cost = models.IntegerField(verbose_name='수업비용', default=10000)
    created_at = models.DateTimeField(verbose_name = '등록일',default=timezone.now)

    
    