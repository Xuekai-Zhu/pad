def solution():
    """Mitzel spent 35% of her allowance. If she spent $14, how much money is left in her allowance?"""
    percentage_spent = 0.35
    amount_spent = 14
    remaining_allowance = (1 - percentage_spent) * amount_spent / percentage_spent
    result = remaining_allowance
    return result

print(solution())