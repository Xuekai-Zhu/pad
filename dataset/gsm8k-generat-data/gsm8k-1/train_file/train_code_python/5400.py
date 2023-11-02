def solution():
    """Lyka wants to buy a smartphone worth $160 but she only has $40 at the moment. 
    She plans to save an equal amount of money per week for two months for the remaining amount that she needs. 
    How much should she save per week?"""
    total_cost = 160
    initial_savings = 40
    weeks_in_two_months = 8
    remaining_cost = total_cost - initial_savings
    savings_per_week = remaining_cost / weeks_in_two_months
    result = savings_per_week
    return result

print(solution())