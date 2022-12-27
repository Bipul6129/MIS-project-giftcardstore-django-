from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import user_invoice
# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class GiftcardType(models.Model):
    name = models.CharField(max_length=100)
    balance = models.CharField(max_length=20)
    price = models.FloatField(default=0.00)
    image = models.ImageField(default='default.png')
    category = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

class Giftcards(models.Model):
    type = models.ForeignKey(GiftcardType,on_delete=models.SET_NULL,null=True)
    # price = models.FloatField(blank=False)
    code = models.CharField(blank=False,max_length=50,unique=True)
    redeemed = models.BooleanField(default=False)
    to = models.CharField(max_length=50,null=True,blank=True)
    posted = models.DateTimeField(default=timezone.now)


@receiver(post_save,sender=Giftcards)
def distribute_giftcard(sender,instance,**kwargs):
    print(instance.type.id)
    checkdelivercount = user_invoice.objects.filter(delivered=False,itemid=instance.type.id).count()
    if checkdelivercount>=1:
        checkdeliver = user_invoice.objects.filter(delivered=False,itemid=instance.type.id).order_by('-created').first()
        print(checkdeliver.user.email)
        Giftcards.objects.filter(id=instance.id).update(to=checkdeliver.user.email,redeemed=True)
        checkdeliver.delivered = True
        checkdeliver.save()
        


    

    



    