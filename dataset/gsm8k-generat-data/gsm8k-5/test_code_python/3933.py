def solution():
    cost = 2 + 8  # Burt spent $2.00 on basil seeds and $8.00 on potting soil
    plants = 20  # The packet of basil seeds yielded 20 basil plants
    price_per_plant = 5  # Burt sells each basil plant for $5.00

    # Calculate the revenue from selling the basil plants
    revenue = plants * price_per_plant

    # Calculate the net profit by subtracting the cost from the revenue
    net_profit = revenue - cost
    result = net_profit
    return result

print(solution())