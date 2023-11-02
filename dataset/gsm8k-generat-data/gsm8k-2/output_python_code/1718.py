def solution():
    """Tonya has $150.00 on her credit card. If she leaves any balance on her card at the end of the month, she is charged 20% interest. If she makes a $50.00 payment on her card, what will be the new balance?"""
    original_balance = 150.00
    payment = 50.00
    remaining_balance = original_balance - payment
    if remaining_balance > 0:
        new_balance = remaining_balance * 1.2
    else:
        new_balance = 0
    result = new_balance
    return result

print(solution())