from django.db import models

# Create your models here.
class Saran(models.Model):
    objectid = models.AutoField(primary_key=True)
    dari = models.CharField(max_length=24)
    sarans = models.TextField()

    def __str__(self):
        return str(self.objectid)