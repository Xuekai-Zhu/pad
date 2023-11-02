def solution():
    # Calculate the total cups of coffee consumed per day
    total_cups_per_day = 3 * 2 + 2

    # Calculate the total ounces of coffee consumed per day
    total_ounces_per_day = total_cups_per_day * 0.5

    # Calculate the total cost of coffee per day
    total_cost_per_day = total_ounces_per_day * 1.25

    # Calculate the total cost of coffee per week
    total_cost_per_week = total_cost_per_day * 7

    result = total_cost_per_week
    return result

print(solution())