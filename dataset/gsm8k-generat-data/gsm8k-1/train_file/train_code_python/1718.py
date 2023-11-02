def solution():
    """Tonya has $150.00 on her credit card. If she leaves any balance on her card at the end of the month, she is charged 20% interest. If she makes a $50.00 payment on her card, what will be the new balance?"""
    balance = 150
    payment = 50
    interest_rate = 0.2
    balance_after_payment = balance - payment
    new_balance = balance_after_payment + (balance_after_payment * interest_rate)
    result = new_balance
    return result

print(solution())