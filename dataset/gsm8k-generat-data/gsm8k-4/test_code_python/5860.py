def solution():
    """Robe's car broke and he used $10 from his savings to pay for the repair. Before the repair, he bought 2 kinds of spare parts. A corner light that costs twice the price of the repair fee, and two brake disks; each disk cost thrice the price of the corner light. After that, he had $480 savings left. How much money did Robe have saved before his car broke?"""
    # Define the initial savings of Robe
    initial_savings = None

    # Define the cost of the repair and the price of the corner light and brake disks
    repair_cost = 10
    corner_light_price = repair_cost * 2
    brake_disk_price = corner_light_price * 3

    # Calculate the total cost of the spare parts
    spare_parts_cost = corner_light_price + (2 * brake_disk_price)

    # Calculate the initial savings of Robe
    initial_savings = spare_parts_cost + repair_cost + 480

    result = initial_savings
    return result

print(solution())