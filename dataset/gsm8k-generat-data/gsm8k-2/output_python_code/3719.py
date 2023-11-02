def solution():
    """A baker sells pastries for $5 and works 7 days a week. On Monday he sold 2. Every day the number of sales increases by 1 compared to the previous day. On average, how many pastries does he sell on each day of the week?"""
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