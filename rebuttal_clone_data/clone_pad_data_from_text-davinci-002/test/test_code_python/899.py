def solution():
    sheared_sheep = 200
    pounds_of_wool_per_sheep = 10
    cost_to_shearer = 2000
    price_per_pound = 20
    total_wool = sheared_sheep * pounds_of_wool_per_sheep
    total_revenue = total_wool * price_per_pound
    total_profit = total_revenue - cost_to_shearer
    result = total_profit
    
    return result

print(solution())