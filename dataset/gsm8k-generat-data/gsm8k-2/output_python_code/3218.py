def solution():
    """Cory bought a patio table and 4 chairs for $135. The patio table cost $55. If each chair cost the same amount, how much did each chair cost?"""
    total_cost = 135
    table_cost = 55
    num_chairs = 4
    chair_cost = (total_cost - table_cost) / num_chairs
    result = chair_cost
    return result

print(solution())