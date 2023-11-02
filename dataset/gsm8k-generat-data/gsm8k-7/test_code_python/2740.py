def solution():
    earnings = 30000
    car_cost = 18000
    trade_in_value = 6000

    # Calculate the total cost of owning the car (not including depreciation)
    total_cost = car_cost - trade_in_value

    # Calculate John's profit
    profit = earnings - total_cost
    result = profit
    return result

print(solution())