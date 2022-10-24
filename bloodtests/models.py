from django.db import models


class Test(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    unit = models.CharField(max_length=50)
    upper = models.IntegerField(blank=True, null=True)
    lower = models.IntegerField(blank=True, null=True)


class TestResult(models.Model):
    pass
