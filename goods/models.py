# models.py
from django.db import models

class Goods(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=255)
    total_quantity = models.IntegerField()
    available_quantity = models.IntegerField()
    issued = models.BooleanField()

class IssuedGoods(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    regno = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=15)
    no_issued = models.IntegerField()
    date_of_issue = models.DateField()
    time_of_issue = models.TimeField()

class StudentLog(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    regno = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=15)
    no_issued = models.IntegerField()
    date_of_issue = models.DateField()
    time_of_issue = models.TimeField()
    returned = models.BooleanField(default=False)
    return_date = models.DateField(null=True, blank=True)
    return_time = models.TimeField(null=True, blank=True)
    penalty = models.IntegerField(null=True, blank=True)
