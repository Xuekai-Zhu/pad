def solution():
    hours_worked = 2 * 4  # Carrie worked for 2 hours a day for 4 days
    hourly_rate = 22  # Carrie was paid $22 an hour
    supply_cost = 54  # The cost for supplies to make the cake was $54

    # Calculate the total cost for labor
    labor_cost = hours_worked * hourly_rate

    # Calculate the total cost for making the cake
    total_cost = labor_cost + supply_cost

    # Calculate the profit earned by Carrie
    profit = 250 - total_cost  # The wedding cake was sold for $250

    result = profit
    return result

print(solution())