def solution():
    """Arthur has $200 in his wallet. He spends four-fifths of that. How much does he have left?"""
    initial_amount = 200
    spent_amount = initial_amount * (4/5)
    remaining_amount = initial_amount - spent_amount
    result = remaining_amount
    return result

print(solution())