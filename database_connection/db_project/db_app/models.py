from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)

    class Meta:
        db_table = "db_app_data"

    def __str__(self):
        return self.name
