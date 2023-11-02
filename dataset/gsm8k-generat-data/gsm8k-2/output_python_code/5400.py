def solution():
    """Lyka wants to buy a smartphone worth $160 but she only has $40 at the moment. She plans to save an equal amount of money per week for two months for the remaining amount that she needs. How much should she save per week?"""
    total_cost = 160
    current_saved = 40
    remaining_cost = total_cost - current_saved
    weeks = 8
    amount_per_week = remaining_cost / weeks
    result = amount_per_week
    return result

print(solution())