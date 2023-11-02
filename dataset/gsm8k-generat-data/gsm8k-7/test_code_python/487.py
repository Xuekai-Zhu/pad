def solution():
    num_pineapples = 6
    pineapple_price = 3
    num_rings_per_pineapple = 12
    ring_price = 5

    # Calculate the total cost of all pineapples
    total_pineapple_cost = num_pineapples * pineapple_price

    # Calculate the total number of pineapple rings
    total_rings = num_pineapples * num_rings_per_pineapple

    # Calculate the total revenue from selling pineapple rings
    total_revenue = (total_rings / 4) * ring_price

    # Calculate the profit by subtracting the total cost from the total revenue
    profit = total_revenue - total_pineapple_cost
    result = profit
    return result

print(solution())