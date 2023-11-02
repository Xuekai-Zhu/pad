def solution():
    
    seed_cost = 2
    soil_cost = 8
    total_cost = seed_cost + soil_cost
    plant_yield = 20
    plant_price = 5
    total_revenue = plant_yield * plant_price
    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())