from django.shortcuts import render

# Create your views here.
import razorpay
from django.conf import settings
from django.views.generic import TemplateView

class PaymentView(TemplateView):
    template_name = 'orders/payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        client = razorpay.Client(auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        ))
        
        # Create a test payment (100 rupees)
        payment = client.order.create({
            'amount': 10000,  # in paise (10000 paise = ₹100)
            'currency': 'INR',
            'payment_capture': '1'
        })
        
        context['payment'] = payment
        context['razorpay_key_id'] = settings.RAZORPAY_KEY_ID
        return context
