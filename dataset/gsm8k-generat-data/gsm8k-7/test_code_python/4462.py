def solution():
    num_bars = 20
    weight_per_bar = 1.5
    cost_per_pound = 0.5

    # Calculate the total weight of all bars of soap
    total_weight = num_bars * weight_per_bar

    # Calculate the total cost of all bars of soap
    total_cost = total_weight * cost_per_pound
    result = total_cost
    return result

print(solution())