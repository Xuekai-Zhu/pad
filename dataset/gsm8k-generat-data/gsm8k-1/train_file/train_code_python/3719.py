def solution():
    """A baker sells pastries for $5 and works 7 days a week. On Monday he sold 2. Every day the number of sales increases by 1 compared to the previous day. On average, how many pastries does he sell on each day of the week?"""
    price_per_pastry = 5
    days_per_week = 7
    initial_sales = 2
    total_sales = sum(range(initial_sales, initial_sales + days_per_week))
    average_sales_per_day = total_sales / days_per_week
    result = average_sales_per_day
    return result

print(solution())