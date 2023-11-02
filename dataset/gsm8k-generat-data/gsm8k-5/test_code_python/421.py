def solution():
    vip_tickets = 2  # Mrs. Wilsborough bought 2 VIP tickets
    regular_tickets = 3  # Mrs. Wilsborough bought 3 regular tickets

    # Calculate the cost of the VIP tickets
    cost_vip_tickets = vip_tickets * 100

    # Calculate the cost of the regular tickets
    cost_regular_tickets = regular_tickets * 50

    # Calculate the total cost of the tickets
    total_cost = cost_vip_tickets + cost_regular_tickets

    # Calculate the remaining savings of Mrs. Wilsborough
    remaining_savings = 500 - total_cost
    result = remaining_savings
    return result

print(solution())