def solution():
    # Cost of the 4-pack of sliced meat
    meat_cost = 40.0

    # Cost of rush delivery (30% of meat cost)
    rush_delivery_cost = meat_cost * 0.3

    # Total cost with rush delivery added
    total_cost = meat_cost + rush_delivery_cost

    # Cost per type of sliced meat
    cost_per_type = total_cost / 4.0
    result = cost_per_type
    return result

print(solution())