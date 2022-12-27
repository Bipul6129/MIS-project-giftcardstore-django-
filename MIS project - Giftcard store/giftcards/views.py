from django.shortcuts import render,redirect
from .models import Giftcards,GiftcardType,Categories
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid 
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.


def landing(request):
    giftcardtypes = GiftcardType.objects.all().order_by('?')
    number_categories = Categories.objects.all().count()
    print(giftcardtypes)
    context = {
        'giftcardtypes':giftcardtypes,
        'number_categories':number_categories,
        
    }
    return render(request,'landing/landing.html',context)

def giftcardtypes(request,pk):

    giftcard = GiftcardType.objects.filter(id=pk).first()
    gift = Giftcards.objects.filter(type=giftcard,redeemed=False).count()
    if gift>=1:
        host = request.get_host()
        invoice = str(uuid.uuid4())
        paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount':giftcard.price,
        'item_name':giftcard.id,
        'invoice':invoice,
        'currency_code':'USD',
        'custom':request.user.id,
        'notify_url':f'http://{host}{reverse("paypal-ipn")}',
        'return_url':f'http://{host}{reverse("paypal-return")}',
        'cancel_return':f'http://{host}{reverse("paypal-cancel")}',

        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        
        context = {
        'giftcardtype':giftcard,
        'form':form,
        }
        return render(request,'landing/giftcardtype.html',context)
    else:
        context = {
        'giftcardtype':giftcard,
        'message':'not in stock'
        }
        return render(request,'landing/giftcardtype.html',context)

    
    

    
def paypal_success(request):
    return render(request,'landing/success.html')

def paypal_cancel(request):
    return render(request,'landing/cancel.html')
    
def categories(request):
    all_categories = Categories.objects.all()
    
    context = {
        'all_category':all_categories
    }
    return render(request,'landing/categories.html',context)
