import stripe

stripe.api_key = 'sk_test_sample'

def process_payment(amount, token):
    try:
        charge = stripe.Charge.create(
            amount=int(amount * 100),
            currency='usd',
            source=token
        )
        return charge
    except stripe.error.CardError as e:
        return None
