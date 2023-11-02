def solution():
    num_packs = 5
    weight_per_pack = 4
    price_per_pound = 5.5

    # Calculate the total weight of beef that James bought
    total_weight = num_packs * weight_per_pack

    # Calculate the total cost of beef that James paid
    total_cost = total_weight * price_per_pound
    result = total_cost
    return result

print(solution())