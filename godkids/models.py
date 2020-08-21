from django.db import models

class Kid(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    residence_state = models.CharField(max_length=2)
    security_code = models.IntegerField()
    gender = models.CharField(max_length=1)
    created = models.DateTimeField()
    
    def __str__(self):
        return self.name
