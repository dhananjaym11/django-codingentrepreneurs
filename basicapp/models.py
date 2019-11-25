from django.db import models

# Create your models here.
class Basicapp(models.Model):
    title =  models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(blank=True, null=True)     #blank-no required field; null- in db null allowed
    featured = models.BooleanField()