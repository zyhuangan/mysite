from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now()-datetime.timedelta(days=1)


class Choice(models.Model):
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

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

#class t_apk_system_config(models.Model):
#	project=models.CharField(max_length=30)
#	version=models.CharField(max_length=20)
#	systemSize=models.CharField(max_length=11)
#	fixedSize=models.CharField(max_length=11)
#	surplusSize=models.CharField(max_length=11)
#	hdversion=models.CharField(max_length=40)
#	def __str__(self):
#		return self.version
