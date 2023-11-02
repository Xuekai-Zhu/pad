def solution():
    
    large_price = 60
    small_price = 30
    last_month_large = 8
    last_month_small = 4
    this_month_large = last_month_large * 2
    this_month_small = last_month_small * 2
    total_sales = (this_month_large * large_price) + (this_month_small * small_price)
    result = total_sales
    return result

print(solution())