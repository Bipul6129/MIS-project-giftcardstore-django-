from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class user_invoice(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    invoice = models.CharField(max_length=100)
    itemid = models.CharField(max_length=100,default=0)
    created = models.DateTimeField(default=timezone.now)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email