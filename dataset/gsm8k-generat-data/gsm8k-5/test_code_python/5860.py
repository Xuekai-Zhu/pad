def solution():
    repair_fee = 10  # Robe used $10 for the repair
    corner_light = 2 * repair_fee  # The corner light costs twice the price of the repair fee
    brake_disks = 2 * 3 * corner_light  # Two brake disks cost thrice the price of the corner light
    total_cost = repair_fee + corner_light + brake_disks  # Total cost of the repair and parts

    # Calculate Robe's initial savings
    initial_savings = total_cost + 480
    result = initial_savings
    return result

print(solution())