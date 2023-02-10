import os

import stripe
from django.http import JsonResponse
from django.shortcuts import render
from dotenv import load_dotenv
from .models import Item

load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
pk_test = os.getenv('STRIPE_PUBLIC_KEY')

def buy_item(request, item_id):
    item = Item.objects.get(id=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name
                },
                'unit_amount': int(item.price),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url="http://localhost:8000/success.html",
        cancel_url="http://localhost:8000/cancel.html",
    )
    return JsonResponse({"session_id": session.id})

def show_item(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, "index.html", {"item": item})
