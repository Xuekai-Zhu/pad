def solution():
    # Calculate the total cost of buying 6 pineapples
    cost_of_pineapples = 6 * 3

    # Calculate the total number of pineapple rings
    total_pineapple_rings = 6 * 12

    # Calculate the total revenue from selling 4 pineapple rings for $5 each
    total_revenue = (total_pineapple_rings // 4) * 5

    # Calculate the profit
    profit = total_revenue - cost_of_pineapples
    result = profit
    return result

print(solution())