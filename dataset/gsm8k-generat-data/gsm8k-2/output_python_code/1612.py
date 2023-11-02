def solution():
    """John is a door-to-door salesman. He visits 50 houses a day. 20% of them buy something from them. Of those that buy something half buy a $50 set of knives and the other half buy a $150 set of knives. How much does he sell a week when he works 5 days a week?"""
    houses_per_day = 50
    percent_buying = 0.2
    sets_per_buyer = 0.5
    low_price = 50
    high_price = 150
    days_per_week = 5
    sales_per_day = houses_per_day * percent_buying
    low_sales_per_day = sales_per_day * sets_per_buyer
    high_sales_per_day = sales_per_day * sets_per_buyer
    total_sales_per_day = (low_sales_per_day * low_price) + (high_sales_per_day * high_price)
    total_sales_per_week = total_sales_per_day * days_per_week
    result = total_sales_per_week
    return result

print(solution())