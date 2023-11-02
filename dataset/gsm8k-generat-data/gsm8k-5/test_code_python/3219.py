def solution():
    total_cost = 135  # Cory bought a patio table and 4 chairs for $135
    table_cost = 55  # The patio table cost $55
    chairs_count = 4  # Cory bought 4 chairs

    # Calculate the total cost of the chairs
    chairs_cost = total_cost - table_cost

    # Calculate the cost of each chair
    chair_cost = chairs_cost / chairs_count
    result = chair_cost
    return result

print(solution())