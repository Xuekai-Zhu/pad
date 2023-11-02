def solution():
    """A bicycle shop owner adds 3 bikes to her stock every week. After 1 month, she had sold 18 bikes but still had 45 bikes in stock. How many bikes did she have originally?"""
    bikes_added_per_week = 3
    weeks_in_month = 4
    bikes_sold_in_month = 18
    bikes_in_stock = 45
    original_bikes = bikes_in_stock + bikes_sold_in_month - (weeks_in_month * bikes_added_per_week) 
    result = original_bikes
    return result

print(solution())