def solution():
    # Define the variables
    oven_power = 500
    heater_power = oven_power / 2
    fridge_power = heater_power * 3

    total_power = oven_power + heater_power + fridge_power

    # Calculate the total amount paid for power in a month
    # Assuming a rate of $0.10 per unit of power
    total_cost = total_power * 0.10
    result = total_cost
    return result

print(solution())