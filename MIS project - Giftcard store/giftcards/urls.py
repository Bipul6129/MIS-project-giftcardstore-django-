from django.urls import path
from .import views

urlpatterns = [
    path('',views.landing,name='landing-page'),
    path('giftcardtype/<int:pk>/',views.giftcardtypes,name='giftcardtype'),
    path('paypal-return',views.paypal_success, name='paypal-return'),
    path('paypal-cancel',views.paypal_cancel, name='paypal-cancel'),
    path('categories/',views.categories,name='giftcardcategories')
]