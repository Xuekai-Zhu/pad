def solution():
    # Calculate the total amount of coffee used by the household per day
    total_coffee_per_day = 3 * 2 * 0.5 + 1 * 2 * 0.5  # James drinks 2 cups + 3 others drink 2 cups each, and each cup uses 0.5 ounces of coffee
    # Calculate the total amount of coffee used by the household per week
    total_coffee_per_week = total_coffee_per_day * 7
    # Calculate the cost of the coffee per week
    cost_per_week = total_coffee_per_week * 1.25  # coffee costs $1.25 per ounce
    result = cost_per_week
    return result

print(solution())