def solution():
    charms_per_necklace = 10  # Tim uses 10 charms to make each necklace
    cost_per_charm = 15  # Each charm costs $15
    selling_price = 200  # Tim sells each necklace for $200
    necklaces_to_sell = 30  # Tim wants to sell 30 necklaces

    # Calculate the total cost of making the necklaces
    total_cost = charms_per_necklace * cost_per_charm * necklaces_to_sell

    # Calculate the total revenue from selling the necklaces
    total_revenue = selling_price * necklaces_to_sell

    # Calculate the profit from selling the necklaces
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())