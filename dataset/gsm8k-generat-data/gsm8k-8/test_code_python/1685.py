def solution():
    # Define the cost of the burger meal and the cost of upgrading the fries and drink
    burger_meal_cost = 6.00
    upgrade_cost = 1.00

    # Calculate the total cost of each day's meal
    daily_cost = burger_meal_cost + upgrade_cost

    # Calculate the total cost of 5 days of meals
    total_cost = daily_cost * 5
    result = total_cost
    return result

print(solution())