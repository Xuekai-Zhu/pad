def solution():
    """Lyra has an $80 budget for a week to spend on food. If she bought 1 bucket of fried chicken that costs $12 and 5 pounds of beef that cost $3 per pound. How much is left on her weekly budget?"""
    budget = 80
    fried_chicken_cost = 12
    beef_cost = 3 * 5
    total_cost = fried_chicken_cost + beef_cost
    remaining_budget = budget - total_cost
    result = remaining_budget
    return result

print(solution())