def solution():
    """Robe's car broke and he used $10 from his savings to pay for the repair. Before the repair, he bought 2 kinds of spare parts. A corner light that costs twice the price of the repair fee, and two brake disks; each disk cost thrice the price of the corner light. After that, he had $480 savings left. How much money did Robe have saved before his car broke?"""
    # Define the cost of the repair
    repair_cost = 10

    # Calculate the cost of the corner light
    corner_light_cost = repair_cost * 2

    # Calculate the cost of a single brake disk
    brake_disk_cost = corner_light_cost * 3

    # Calculate the total cost of the spare parts
    spare_parts_cost = corner_light_cost + 2 * brake_disk_cost

    # Calculate the initial savings
    initial_savings = spare_parts_cost + repair_cost + 480

    # Display the initial savings
    result = initial_savings
    return result

print(solution())