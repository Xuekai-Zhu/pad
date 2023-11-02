def solution():
    total_budget = 80  # Lyra has an $80 budget for a week
    chicken_cost = 12  # Lyra bought 1 bucket of fried chicken that costs $12
    beef_cost = 5 * 3  # Lyra bought 5 pounds of beef that cost $3 per pound

    # Calculate the total amount spent on food
    total_spent = chicken_cost + beef_cost

    # Calculate the amount left on Lyra's weekly budget
    remaining_budget = total_budget - total_spent
    result = remaining_budget
    return result

print(solution())