def solution():
    """Leila spent 3/4 of her savings on make-up and the rest on a sweater. If the sweater cost her $20, what were her original savings?"""
    sweater_cost = 20
    percent_spent = 3/4
    remaining_percent = 1 - percent_spent
    remaining_money = sweater_cost / remaining_percent
    original_savings = remaining_money / percent_spent
    result = original_savings
    return result

print(solution())