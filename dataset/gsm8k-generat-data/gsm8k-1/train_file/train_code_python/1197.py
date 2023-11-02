def solution():
    """Arthur has $200 in his wallet. He spends four-fifths of that. How much does he have left?"""
    wallet_total = 200
    spent_fraction = 4/5
    amount_spent = wallet_total * spent_fraction
    amount_left = wallet_total - amount_spent
    result = amount_left
    return result

print(solution())