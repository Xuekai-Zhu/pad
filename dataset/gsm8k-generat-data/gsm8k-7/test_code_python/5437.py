def solution():
    num_packs = 4
    pack_cost = 40.0
    rush_delivery_percent = 0.3  # 30% rush delivery fee

    # Calculate the total cost of the meat packs with rush delivery
    total_cost = pack_cost + (pack_cost * rush_delivery_percent)

    # Calculate the cost per type of sliced meat
    cost_per_type = total_cost / num_packs
    result = cost_per_type
    return result

print(solution())