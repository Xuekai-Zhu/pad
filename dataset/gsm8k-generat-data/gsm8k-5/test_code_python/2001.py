def solution():
    # Calculate the total distance traveled
    distance_first_leg = 60 * 2  # Jenna drives 60 miles per hour for 2 hours
    distance_second_leg = 50 * 3  # Jenna drives 50 miles per hour for 3 hours
    total_distance = distance_first_leg + distance_second_leg

    # Calculate the total amount of gas needed
    gas_needed = total_distance / 30  # Jenna can drive 30 miles on one gallon of gas

    # Calculate the total cost of gas
    gas_cost_per_gallon = 2
    total_gas_cost = gas_needed * gas_cost_per_gallon

    result = total_gas_cost
    return result

print(solution())