from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

class t_apk_system_config(models.Model):
        project = models.CharField(max_length=30, blank=True, null=True)
        version = models.CharField(max_length=20, blank=True, null=True)
        systemsize = models.IntegerField(db_column='systemSize', blank=True, null=True)  # Field name made lowercase.
        fixedsize = models.IntegerField(db_column='fixedSize', blank=True, null=True)  # Field name made lowercase.
        surplussize = models.IntegerField(db_column='surplusSize', blank=True, null=True)  # Field name made lowercase.
        hdversion = models.CharField(max_length=40, blank=True, null=True)

        class Meta:
                managed = False
                db_table = 't_apk_system_config'
