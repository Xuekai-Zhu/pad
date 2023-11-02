def solution():
    """John buys 20 bars of soap each weighing 1.5 pounds for $.5 per pound. How much money did he spend on soap?"""
    num_bars = 20
    weight_per_bar = 1.5
    price_per_pound = 0.5
    total_weight = num_bars * weight_per_bar
    total_cost = total_weight * price_per_pound
    result = total_cost
    return result

print(solution())