def solution():
    
    price_per_pastry = 5
    days_per_week = 7
    initial_sales = 2
    total_sales = sum(range(initial_sales, initial_sales + days_per_week))
    average_sales_per_day = total_sales / days_per_week
    result = average_sales_per_day
    return result

print(solution())