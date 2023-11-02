def solution():
    total_cost = 130 - 4  # Jude paid $130 and got $4 change
    table_cost = 50  # Table cost $50
    plate_cost = 2 * 20  # Two sets of plates at $20 each

    # Calculate the cost of three chairs
    chair_cost = total_cost - table_cost - plate_cost
    cost_per_chair = chair_cost / 3
    result = cost_per_chair
    return result

print(solution())