def solution():
    # Define the number of liters filled today and on Friday
    liters_today = 10
    liters_friday = 25

    # Define the cost per liter of gas today and calculate the cost for today's purchase
    cost_today = 1.4 * liters_today

    # Define the cost per liter of gas on Friday after the rollback and calculate the cost for Friday's purchase
    cost_friday = 1.4 - 0.4
    cost_friday *= liters_friday

    # Calculate the total cost for both purchases
    total_cost = cost_today + cost_friday
    result = total_cost
    return result

print(solution())