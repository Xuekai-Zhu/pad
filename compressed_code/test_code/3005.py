def solution():
    
    bikes_added_per_week = 3
    weeks_in_month = 4
    bikes_sold_in_month = 18
    bikes_in_stock = 45
    original_bikes = bikes_in_stock + bikes_sold_in_month - (weeks_in_month * bikes_added_per_week) 
    result = original_bikes
    return result

print(solution())