def solution():
    num_days = 2
    num_gas_stations = 4
    gas_prices = [3, 3.5, 4, 4.5]
    tank_size = 12

    # Calculate the total cost of gas for each day
    total_cost_per_day = []
    for i in range(num_days):
        cost_per_day = 0
        for j in range(num_gas_stations):
            cost_per_day += gas_prices[j] * tank_size
        total_cost_per_day.append(cost_per_day)

    # Calculate the total cost of gas for the entire road trip
    total_cost = sum(total_cost_per_day)
    result = total_cost
    return result

print(solution())