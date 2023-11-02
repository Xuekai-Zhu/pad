def solution():
    
    pastry_price = 2
    bread_price = 4
    daily_avg = (20 * pastry_price) + (10 * bread_price)
    today_sales = (14 * pastry_price) + (25 * bread_price)
    difference = today_sales - daily_avg
    result = difference
    return result

print(solution())