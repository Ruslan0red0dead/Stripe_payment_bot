import stripe

STRIPE_SECRET_KEY = ''
stripe.api_key = STRIPE_SECRET_KEY

def payment_details():
    amount = 1000  # Amount in cents
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Payment via Telegram bot',
                },
                'unit_amount': amount,
            },
            'quantity': 1,
        }],
        mode='payment',
        # be sure to enter success_url and cancel_url
        # is a redirect after successful or unsuccessful payment
        success_url='',
        cancel_url=''
    )
    return checkout_session.url