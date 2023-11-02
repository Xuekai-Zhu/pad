def solution():
    # Define the prices and costs
    haircut_price = 30
    perm_price = 40
    dye_price = 60
    dye_cost = 10

    # Calculate the total revenue and costs
    total_revenue = 4 * haircut_price + 1 * perm_price + 2 * dye_price
    total_cost = 2 * dye_cost

    # Calculate the net profit
    net_profit = total_revenue - total_cost + 50
    result = net_profit
    return result

print(solution())