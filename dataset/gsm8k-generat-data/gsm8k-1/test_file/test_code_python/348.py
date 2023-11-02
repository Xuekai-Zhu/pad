def solution():
    """After Andrea saved some money, she then spent the rest of her money on an $11 sweater and gave her brother $4. If she had $36 in the beginning, how much did Andrea save?"""
    starting_amount = 36
    sweater_cost = 11
    brother_gift = 4
    remaining_amount = starting_amount - sweater_cost - brother_gift
    amount_saved = starting_amount - remaining_amount
    result = amount_saved
    return result

print(solution())