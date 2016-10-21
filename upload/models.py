from __future__ import unicode_literals

from django.db import models

# Create your models here.

# User CLass for user , username and usering path 
class NormalUser(models.Model):
        version = models.CharField(max_length=128)
        ownername = models.CharField(max_length=30)
        isofile = models.FileField(upload_to='./upload_place')
        state = models.CharField(max_length=10)
	release = models.CharField(max_length=10) 

        def __unicode__(self):
                return self.version

        def __unicode__(self):
                return self.ownername

        def __unicode__(self):
                return self.state
	
	def __unicode__(self):
		return self.release

