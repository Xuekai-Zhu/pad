def solution():
    """James finds 3 bills in his pocket. They are all 20s. If he already had $75 in his wallet how much money doe he have now?"""
    num_bills = 3
    bill_value = 20
    current_wallet_value = 75
    new_wallet_value = current_wallet_value + (num_bills * bill_value)
    result = new_wallet_value
    return result

print(solution())