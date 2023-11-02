def solution():
    # Calculate the total revenue from selling basil plants
    num_plants = 20
    price_per_plant = 5
    total_revenue = num_plants * price_per_plant

    # Calculate the total cost of producing the basil plants
    total_cost = 2 + 8  # $2 for seeds and $8 for soil

    # Calculate the net profit
    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())