from operator import truediv
from django.db import models
from django.urls import reverse


class Paste(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=40, null=True,blank= True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('pastebin:paste_detail', kwargs={'pk': self.pk})       	