# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
#from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=30)
    texts = models.TextField()
    created_date =models.DateTimeField(default = timezone.now)
    objects = models.Manager()

    def __str__(self):
        return self.name
    
    #def get_absolute_url(self):
     #   return reverse("todo_list:about", kwargs={"id" : self.id})

