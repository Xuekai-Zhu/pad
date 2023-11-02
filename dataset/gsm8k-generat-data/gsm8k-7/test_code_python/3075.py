def solution():
    num_boxes = 5
    candy_bars_per_box = 10
    sell_price = 1.5
    cost_price = 1.0

    # Calculate the total number of candy bars James is selling
    total_candy_bars = num_boxes * candy_bars_per_box

    # Calculate the total sales revenue from selling the candy bars
    total_sales_revenue = total_candy_bars * sell_price

    # Calculate the total cost of buying the candy bars
    total_cost = total_candy_bars * cost_price

    # Calculate the profit from these sales
    profit = total_sales_revenue - total_cost
    result = profit
    return result

print(solution())