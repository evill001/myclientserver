from django.db import models


class Books(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    read = models.BooleanField(default=True)

    def __str__(self):
        return self.title