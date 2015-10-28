# coding:utf-8
import sys
from django.db import models
from django.utils import timezone
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')


# Create your models here.
class Requirement(models.Model):
    def __str__(self):
        return self.requirement_desc

    enroll_date = models.DateField("录入时间", auto_now_add=True)
    pd_owner = models.CharField("产品负责人", max_length=20)
    business_type = models.CharField("业务类型", max_length=100)
    requirement_desc = models.TextField('需求描述')
    solution = models.TextField('解决方案')
    estimate_solute_date = models.DateField('预计解决时间')
    actual_solute_date = models.DateField('实际解决时间', blank=True, null=True)
    requirement_type = models.CharField('需求类型', max_length=100)
    requirement_source = models.CharField('需求来源', max_length=100)
    requirement_status = models.CharField('需求状态', max_length=100)
    comments = models.TextField('备注', blank=True, null=True)

    def was_resolved_on_time(self):
        # now = timezone.now()
        now = datetime.date.today()
        return self.actual_solute_date == now
        # return now - datetime.timedelta(days=1) <= self.enroll_date <= now

    was_resolved_on_time.admin_order_field = 'actual_solute_date'
    was_resolved_on_time.boolean = True
    was_resolved_on_time.short_description = '到期是否已解决？'


class BugsOnLine(models.Model):
    def __str__(self):
        return self.bug_desc

    report_date = models.DateTimeField("提交时间", auto_now_add=True)
    pd_owner = models.CharField("产品负责人", max_length=20, blank=True, null=True)
    bug_status = models.CharField("状态", max_length=20)
