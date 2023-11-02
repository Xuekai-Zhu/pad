def solution():
    num_pairs = 9
    socks_price = 2
    profit_percentage = 0.25
    profit_per_pair = 0.2
    num_pairs_with_percentage_profit = 4
    num_pairs_with_fixed_profit = 5

    # Calculate the total revenue from all sock sales
    total_revenue = num_pairs * socks_price

    # Calculate the revenue from the pairs with percentage profit
    revenue_percentage_profit = num_pairs_with_percentage_profit * socks_price * (1 + profit_percentage)

    # Calculate the revenue from the pairs with fixed profit
    revenue_fixed_profit = num_pairs_with_fixed_profit * (socks_price + profit_per_pair)

    # Calculate the total profit from all sock sales
    total_profit = (revenue_percentage_profit + revenue_fixed_profit) - total_revenue
    result = total_profit
    return result

print(solution())