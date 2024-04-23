from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length = 255)
    localstname = models.CharField(max_length = 255)