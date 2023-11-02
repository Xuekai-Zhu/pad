def solution():
    """Lyra has an $80 budget for a week to spend on food. If she bought 1 bucket of fried chicken that costs $12 and 5 pounds of beef that cost $3 per pound. How much is left on her weekly budget?"""
    food_budget = 80
    chicken_cost = 12
    beef_cost = 3
    beef_pounds = 5
    total_spent = chicken_cost + (beef_cost * beef_pounds)
    remaining_budget = food_budget - total_spent
    result = remaining_budget
    return result

print(solution())