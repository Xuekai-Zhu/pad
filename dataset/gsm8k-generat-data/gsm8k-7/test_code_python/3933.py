def solution():
    seed_cost = 2.0
    soil_cost = 8.0
    num_plants = 20
    plant_price = 5.0

    # Calculate the total revenue from selling all basil plants
    total_revenue = num_plants * plant_price

    # Calculate the total cost of producing all basil plants
    total_cost = seed_cost + soil_cost

    # Calculate the net profit
    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())