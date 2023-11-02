def solution():
    candy_bars_per_box = 10
    boxes_sold = 5
    cost_per_bar = 1
    selling_price_per_bar = 1.5

    # Calculate the total cost to buy the candy bars
    total_cost = candy_bars_per_box * boxes_sold * cost_per_bar

    # Calculate the total revenue from selling the candy bars
    total_revenue = candy_bars_per_box * boxes_sold * selling_price_per_bar

    # Calculate the profit from the sales
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())