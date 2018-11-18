# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class comment(models.Model):
    text= models.CharField(max_length=480)
    name= models.CharField(max_length =120)
    email= models.EmailField()
    
    def __str__(self):
        return (self.name,self.text)


class Message(models.Model):

    title = models.CharField(max_length = 120)
    text = models.TextField()

    # class Meta:
    #     verbose_name = "message"
    # #     verbose_name_plural = "messages"
    # def get_absolute_url(self):
    #     return reverse('commview', args=(self.pk,))
    def __str__(self):
        return self.title

    