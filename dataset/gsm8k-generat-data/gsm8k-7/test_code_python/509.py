def solution():
    electricity_price = 0.10
    consumption_rate = 2.4
    num_hours = 25

    # Calculate the total consumption in kilowatt-hours
    total_consumption = consumption_rate * num_hours

    # Calculate the total cost of electricity used by the oven
    total_cost = total_consumption * electricity_price
    result = total_cost
    return result

print(solution())