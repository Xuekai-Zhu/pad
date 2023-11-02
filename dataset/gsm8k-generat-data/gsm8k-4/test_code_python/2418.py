def solution():
    """Lyra has an $80 budget for a week to spend on food. If she bought 1 bucket of fried chicken that costs $12 and 5 pounds of beef that cost $3 per pound. How much is left on her weekly budget?"""
    # Define the budget and the cost of chicken and beef
    budget = 80
    chicken_cost = 12
    beef_cost_per_pound = 3

    # Calculate the cost of beef
    beef_cost = 5 * beef_cost_per_pound

    # Calculate the total cost of food
    total_cost = chicken_cost + beef_cost

    # Calculate the remaining budget
    remaining_budget = budget - total_cost

    # Return the result
    result = remaining_budget
    return result

print(solution())