def solution():
    # Define initial amount of money and cost per trip
    initial_money = 200
    cost_per_trip = 2

    # Calculate total cost per month and remaining money after each trip
    monthly_cost = cost_per_trip * 4
    remaining_money = initial_money - monthly_cost

    # Calculate remaining money after a year (12 months)
    remaining_money_after_year = remaining_money * 12
    result = remaining_money_after_year
    return result

print(solution())