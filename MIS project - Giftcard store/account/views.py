from django.shortcuts import render,redirect
from .forms import CreateUserForm,AccountAuthenticationForm
from django.contrib.auth import logout as dj_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as djlogin
from giftcards.models import Giftcards
from .models import user_invoice
# Create your views here.


def signup(request):
    form = CreateUserForm
    if request.user.is_authenticated:
        return redirect('landing-page')
    if request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            context={
                'signup':'Succesfully signed up'
            }
            return render(request,'account/signup.html',context)
        
    context = {
        'form':form,
    }
    return render(request,'account/signup.html',context)

@login_required
def logout(request):
    dj_logout(request)
    return redirect('landing-page')

def login_user(request):
    context = {}
    user=request.user
    if user.is_authenticated:
        return redirect('landing-page')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)

            if user:
                djlogin(request, user)
                return redirect('landing-page')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request,'account/signin.html',context)

@login_required
def mygiftcards(request):
    mygiftcard = Giftcards.objects.filter(to=request.user.email)
    checkdeliver = user_invoice.objects.filter(user=request.user,delivered=False).count()
    # if checkdeliver>=1:
    #     items = user_invoice.objects.filter(user=request.user,delivered=False)
    #     for item in items:
    #         checkgiftcardcount = Giftcards.objects.filter(type=item.itemid,redeemed=False).count()
    #         if checkgiftcardcount>=1:
    #             checkgiftcard= Giftcards.objects.filter(type=item.itemid,redeemed=False).first()
    #             checkgiftcard.to = request.user.email
    #             checkgiftcard.redeemed = True
    #             checkgiftcard.save()
    #             item.delivered=True
    #             item.save()
    #             print(checkgiftcard.code)
        
    #     context = {
    #         'mygiftcard':mygiftcard,
    #         'undelivered':checkdeliver
    #     }
    # else:
    #     context = {
    #         'mygiftcard':mygiftcard
    #     }
    context = {
        'mygiftcard':mygiftcard,
        'undelivered':checkdeliver
    }
    return render(request,'account/mygiftcards.html',context)
