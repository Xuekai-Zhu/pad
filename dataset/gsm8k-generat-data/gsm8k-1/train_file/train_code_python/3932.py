def solution():
    """Burt spent $2.00 on a packet of basil seeds and $8.00 on potting soil. The packet of seeds yielded 20 basil plants. He sells each basil plant for $5.00 at the local farmer's market. What is the net profit from his basil plants?"""
    seed_cost = 2
    soil_cost = 8
    plant_yield = 20
    plant_price = 5
    total_cost = seed_cost + soil_cost
    total_revenue = plant_yield * plant_price
    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())