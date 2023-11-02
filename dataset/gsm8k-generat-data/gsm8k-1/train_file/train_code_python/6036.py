def solution():
    """James finds 3 bills in his pocket. They are all 20s. If he already had $75 in his wallet how much money does he have now?"""
    bills_found = 3
    bill_value = 20
    initial_wallet_amount = 75
    total_found = bills_found * bill_value
    new_wallet_amount = initial_wallet_amount + total_found
    result = new_wallet_amount
    return result

print(solution())