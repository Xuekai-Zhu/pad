def solution():
    
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