def solution():
    # Define the weight and cost of each bar of soap
    weight_per_bar = 1.5
    cost_per_pound = 0.5
    cost_per_bar = weight_per_bar * cost_per_pound

    # Calculate the total cost of all 20 bars of soap
    total_cost = cost_per_bar * 20
    result = total_cost
    return result

print(solution())