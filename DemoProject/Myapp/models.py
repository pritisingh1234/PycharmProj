from django.db import models


class Employees(models.Model):
    e_name = models.CharField(max_length=100)
    e_id = models.IntegerField()

    def __str__(self):
        return self.e_name
