def solution():
    # Define the cost per watt and the amount of electricity used
    cost_per_watt = 4
    electricity_used = 300

    # Calculate the cost of electricity used
    electricity_cost = cost_per_watt * electricity_used

    # Add the late fee
    total_cost = electricity_cost + 150

    result = total_cost
    return result

print(solution())