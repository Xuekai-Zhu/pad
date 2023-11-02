def solution():
    daily_visits = 50  # John visits 50 houses a day
    conversion_rate = 0.2  # 20% of the houses John visits buy something
    knife_sets_sold = (daily_visits * conversion_rate) / 2  # Half of the customers who buy something buy a $50 set of knives and half buy a $150 set
    total_sales_per_day = (knife_sets_sold * 50) + (knife_sets_sold * 150)  # Calculate total sales per day
    weekly_sales = total_sales_per_day * 5  # Calculate total sales for the week (assuming he works 5 days a week)
    result = weekly_sales
    return result

print(solution())