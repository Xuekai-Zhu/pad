def solution():
    # Calculate the cost of one pack of fancy, sliced meat with rush delivery included
    pack_cost = 40  # cost of a 4-pack of fancy, sliced meat
    rush_cost = pack_cost * 0.3  # 30% rush delivery fee
    total_cost = pack_cost + rush_cost  # total cost of one pack with rush delivery included
    cost_per_type = total_cost / 4  # cost per type of sliced meat in one pack
    result = cost_per_type
    return result

print(solution())