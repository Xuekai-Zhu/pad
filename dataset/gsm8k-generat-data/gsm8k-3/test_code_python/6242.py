def solution():
    """Tim drinks 2 bottles that are each 1.5 quarts and an additional 20 ounces a day.  How much water does he drink a week?"""
    
    # Convert bottle size to quarts
    bottle_size = 1.5 * 4
    
    # Calculate total amount of water Tim drinks in a day
    daily_water = (bottle_size * 2) + (20/32)
    
    # Calculate total amount of water Tim drinks in a week (7 days)
    weekly_water = daily_water * 7
    
    result = weekly_water
    return result

print(solution())