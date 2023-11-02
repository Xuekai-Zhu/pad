def solution():
    # Calculate the cost of the curtains
    curtains_cost = 2 * 30

    # Calculate the cost of the wall prints
    wall_prints_cost = 9 * 15

    # Calculate the total cost without installation
    total_cost = curtains_cost + wall_prints_cost

    # Add the cost of the installation service
    total_cost_with_installation = total_cost + 50

    result = total_cost_with_installation
    return result

print(solution())