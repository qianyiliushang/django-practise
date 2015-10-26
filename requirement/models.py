# coding:utf-8
import sys
from django.db import models
from django.utils import timezone

reload(sys)
sys.setdefaultencoding('utf-8')


# Create your models here.
class Requirement(models.Model):
    enroll_date = models.DateTimeField("录入时间", default=timezone.datetime)
    pd_owner = models.CharField("产品负责人", max_length=20)
    business_type = models.CharField("业务类型", max_length=100)
    requirement_desc = models.TextField('需求描述')
    solution = models.TextField('解决方案')
    estimate_solute_date = models.DateField('预计解决时间')
    actual_solute_date = models.DateField('实际解决时间')
    requirement_type = models.CharField('需求类型', max_length=100)
    requirement_source = models.CharField('需求来源', max_length=100)
    requirement_status = models.CharField('需求状态', max_length=100)
