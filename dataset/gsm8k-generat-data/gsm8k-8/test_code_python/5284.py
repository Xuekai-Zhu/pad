def solution():
    # Calculate the total number of eggs per day
    eggs_per_day = 8 * 3

    # Calculate the number of eggs per week
    eggs_per_week = eggs_per_day * 7

    # Calculate the number of dozens of eggs per week
    dozens_per_week = eggs_per_week / 12

    # Calculate the total revenue per week
    revenue_per_week = dozens_per_week * 5

    # Calculate the total revenue for 4 weeks
    total_revenue = revenue_per_week * 4

    # Round the result to two decimal places
    result = round(total_revenue, 2)
    return result

print(solution())