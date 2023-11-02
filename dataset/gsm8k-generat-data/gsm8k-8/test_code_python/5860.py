def solution():
    # Define the cost of the repair and the corner light
    repair_cost = 10
    corner_light_cost = repair_cost * 2

    # Define the cost of the two brake disks
    brake_disks_cost = corner_light_cost * 3

    # Calculate the total cost
    total_cost = repair_cost + corner_light_cost + brake_disks_cost

    # Calculate the initial savings
    initial_savings = total_cost + 480
    result = initial_savings

    return result

print(solution())