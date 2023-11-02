def solution():
    
    candy_bars_per_box = 10
    boxes_sold = 5
    selling_price = 1.5
    buying_price = 1
    total_candy_bars_sold = candy_bars_per_box * boxes_sold
    revenue = total_candy_bars_sold * selling_price
    cost = total_candy_bars_sold * buying_price
    profit = revenue - cost
    result = profit
    return result

print(solution())