def solution():
    boxes_sold = 5
    candy_bars_per_box = 10
    sale_price_per_bar = 1.50
    cost_per_bar = 1
    total_sales = boxes_sold * candy_bars_per_box * sale_price_per_bar
    total_cost = boxes_sold * candy_bars_per_box * cost_per_bar
    profit = total_sales - total_cost
    result = profit
    return result

print(solution())