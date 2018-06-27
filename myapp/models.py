from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=100,null=True)
	author = models.CharField(max_length=100,null=True)
	abstract = models.CharField(max_length=500,null=True)
	document = models.FileField(upload_to='documents/', blank=True)	

	# document = models.FileField(upload_to='documents/%Y/%m/%d/',blank=True)

    # uploaded_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "id: {}, {}".format(self.id, self.name)
    
	def __unicode__(self):
		return u"%s"%(self.name)
# class Person(models.Model):
# 	name=models.CharField(max_length=100)
# 	image=models.ImageField(upload_to='images',default='\images\icon-user-default.png')
# 	department=models.CharField(max_length=100,blank=True,null=True)
# 	phone_number = models.CharField(max_length=20,null=True)
# 	document = models.FileField(upload_to='documents/', blank=True)	
# 	# document = models.FileField(upload_to='documents/%Y/%m/%d/',blank=True)

#     # uploaded_at = models.DateTimeField(auto_now_add=True)

    
# 	def __unicode__(self):
# 		return u"%s"%(self.name)

# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='documents/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)