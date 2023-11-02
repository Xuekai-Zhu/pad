def solution():
    # Calculate the total cost of the pineapples
    pineapple_cost = 6 * 3

    # Calculate the total number of pineapple rings Jonah could make
    total_rings = 6 * 12

    # Calculate the total revenue Jonah received from selling the pineapple rings
    total_revenue = (total_rings / 4) * 5

    # Calculate the profit Jonah made
    profit = total_revenue - pineapple_cost
    result = profit
    return result

print(solution())