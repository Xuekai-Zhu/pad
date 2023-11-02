def solution():
    cost_per_bushel = 12.0
    num_apples_per_bushel = 48
    sell_price_per_apple = 0.40
    num_apples_sold = 100

    # Calculate the cost to buy one apple from the farmer
    cost_per_apple = cost_per_bushel / num_apples_per_bushel

    # Calculate the revenue from selling 100 apples to the stores
    revenue = num_apples_sold * sell_price_per_apple

    # Calculate the cost of buying 100 apples from the farmer
    cost = num_apples_sold * cost_per_apple

    # Calculate the profit made from selling 100 apples
    profit = revenue - cost
    result = profit
    return result

print(solution())