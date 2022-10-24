from django.db import models


class Test(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    upper = models.FloatField(blank=True, null=True)
    lower = models.FloatField(blank=True, null=True)


class TestResult(models.Model):
    pass
