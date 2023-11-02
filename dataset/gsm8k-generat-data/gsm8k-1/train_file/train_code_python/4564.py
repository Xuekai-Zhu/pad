def solution():
    """Yoque borrowed money from her sister. She promised to pay it back in 11 months including an additional 10% of the money she borrowed. If she pays $15 per month, how much money did she borrow?"""
    total_months = 11
    additional_percent = 10
    monthly_payment = 15
    total_payment = total_months * monthly_payment
    amount_paid_back = total_payment - (total_payment * (additional_percent / 100))
    borrowed_amount = amount_paid_back / (1 + (additional_percent / 100))
    result = borrowed_amount
    return result

print(solution())