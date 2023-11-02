def solution():
    """The water pressure of a sink has a steady flow of 2 cups per 10 minutes for the first 30 minutes. 
    It still flows at 2 cups per 10 minutes for the next 30 minutes after. For the next hour, 
    the water pressure maximizes to 4 cups per 10 minutes and stops. Shawn now has to dump half of the water away. 
    How much water is left?"""
    # Calculate the total amount of water that flows during the first hour (in cups)
    first_hour_water = 2 * 3 * 6
    
    # Calculate the total amount of water that flows during the next hour (in cups)
    second_hour_water = 4 * 6 * 6
    
    # Add the water from the first and second hour
    total_water = first_hour_water + second_hour_water
    
    # Dump half of the water away
    total_water = total_water / 2
    
    # return the result
    result = total_water
    return result

print(solution())