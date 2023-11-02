def solution():
    # Calculate the total cost of 10 liters of gas today and 25 liters of gas on Friday
    cost_today = 10 * 1.4  # cost per liter of gas is $1.4 today
    cost_friday = 25 * 1.4 * 0.6  # after the $0.4 oil price rollback
    total_cost = cost_today + cost_friday
    result = total_cost
    return result

print(solution())