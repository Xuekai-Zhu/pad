def solution():
    bikes_added_per_week = 3
    bikes_sold_per_month = 18
    bikes_in_stock_per_month = 45
    bikes_in_stock_per_week = bikes_in_stock_per_month / 4
    bikes_added_per_month = bikes_added_per_week * 4
    bikes_in_stock_initially = bikes_in_stock_per_month + bikes_added_per_month - bikes_sold_per_month
    result = bikes_in_stock_initially
    
    return result

print(solution())