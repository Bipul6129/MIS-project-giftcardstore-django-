from django.shortcuts import get_object_or_404
from paypal.standard.ipn.signals import valid_ipn_received,invalid_ipn_received
from django.dispatch import receiver
from account.models import user_invoice
from .models import Giftcards,GiftcardType
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .import views

@receiver(valid_ipn_received)
def valid_ipn_signal(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        print(ipn.invoice)
        print("success")
        print(ipn.custom)
        user_invoice.objects.create(user_id=ipn.custom,invoice=ipn.invoice,itemid=ipn.item_name)
        code = Giftcards.objects.filter(type=ipn.item_name,redeemed=False).first()
        buyer = User.objects.filter(id=ipn.custom).first()
        codecount = Giftcards.objects.filter(type=ipn.item_name,redeemed=False).count()
        if codecount<1:
            print("no code")
        else:
            code.to = buyer.email
            code.redeemed = True
            code.save()
            deliverinvoice = user_invoice.objects.filter(invoice=ipn.invoice).first()
            deliverinvoice.delivered = True
            deliverinvoice.save()
       


        

# @receiver(invalid_ipn_received)
# def invalid_ipn_signal(sender, **kwargs):
#     ipn = sender
#     if ipn.payment_status == 'Completed':
#         # payment was successful
#         print(ipn.invoice)
#         print("success")
#         print(ipn.custom)
#         user_invoice.objects.create(user_id=ipn.custom,invoice=ipn.invoice)