from __future__ import unicode_literals

from django.db import models



class Saikorian(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    rollNumber=models.IntegerField(blank=False, null=False,unique=True)
    donation=models.DecimalField(null=True, max_digits=10, decimal_places=2,default=0) 
    description=models.TextField(blank=True)
    emailId=models.EmailField(blank=True)
    
    class Meta:
        ordering = ('donation',)