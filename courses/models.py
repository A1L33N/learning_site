from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model): #extend from base Model class
    created_at = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self): #to configure how python shell returns queries
        return self.title


class Step(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)
    content = models.TextField(blank = True, default = "")

    class Meta:
        ordering = ['order',]   #handles ordering

    def __str__(self):
        return ('{}: {}'.format(self.order, self.title))
