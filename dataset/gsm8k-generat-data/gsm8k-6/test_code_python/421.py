def solution():
    # Calculate the total cost of tickets
    VIP_cost = 2 * 100
    regular_cost = 3 * 50
    total_cost = VIP_cost + regular_cost

    # Calculate Mrs. Wilsborough's remaining savings
    remaining_savings = 500 - total_cost
    result = remaining_savings
    return result

print(solution())