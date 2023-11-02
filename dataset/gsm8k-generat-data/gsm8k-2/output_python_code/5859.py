def solution():
    """Robe's car broke and he used $10 from his savings to pay for the repair. Before the repair, he bought 2 kinds of spare parts.
    A corner light that costs twice the price of the repair fee, and two brake disks; each disk cost thrice the price of the corner light.
    After that, he had $480 savings left. How much money did Robe have saved before his car broke?"""
    repair_cost = 10
    corner_light_cost = 2 * repair_cost
    brake_disk_cost = 3 * corner_light_cost
    total_parts_cost = corner_light_cost + (2 * brake_disk_cost)
    total_savings = total_parts_cost + repair_cost + 480
    result = total_savings
    return result

print(solution())