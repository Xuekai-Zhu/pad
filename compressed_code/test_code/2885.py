def solution():
    
    pastry_price = 5
    days_worked = 7
    first_day_sales = 2
    total_sales = 0
    for i in range(days_worked):
        daily_sales = first_day_sales + i
        total_sales += daily_sales
    average_sales_per_day = total_sales / days_worked
    result = average_sales_per_day
    return result

print(solution())