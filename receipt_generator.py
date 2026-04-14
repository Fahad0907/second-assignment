def generate_receipt(charge_id, user_email):
    receipt = {
        'id': charge_id,
        'date': datetime.now(),
        'email': user_email,
        'amount': charge_id.amount / 100
    }
    send_receipt_email(user_email, receipt)
    return receipt
