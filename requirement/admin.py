# coding:utf-8
from django.contrib import admin
from .models import Requirement
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# Register your models here.




class RequirementAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['enroll_date', 'pd_owner', ]}),
        ('需求详情', {'fields': ['business_type', 'requirement_desc', 'requirement_type', 'requirement_source',
                             'requirement_status']}),
        ('解决方案', {'fields': ['solution', 'estimate_solute_date', 'actual_solute_date']}),
        ('其它',{'fields':['comments']}),

    ]

    list_display = ('requirement_desc', 'pd_owner', 'enroll_date', 'estimate_solute_date', 'was_resolved_on_time')


admin.site.register(Requirement, RequirementAdmin)
