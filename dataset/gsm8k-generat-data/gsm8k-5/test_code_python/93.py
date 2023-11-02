def solution():
    # Calculate the cost of the beef
    beef_cost = 1000 * 8  # John orders 1000 pounds of beef for $8 per pound

    # Calculate the cost of the chicken
    chicken_cost = 2 * 1000 * 3  # John orders twice the amount of chicken as the beef, at $3 per pound

    # Calculate the total cost
    total_cost = beef_cost + chicken_cost
    result = total_cost
    return result

print(solution())