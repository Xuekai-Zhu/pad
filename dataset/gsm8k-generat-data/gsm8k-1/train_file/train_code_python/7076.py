def solution():
    """Boston had .5 feet of snow on the first day of winter. 
    The next day they got an additional 8 inches. 
    Over the next 2 days, 2 inches of the snow melted. 
    On the fifth day, they received another 2 times the amount of snow they received on the first day. 
    How many feet of snow do they now have?"""
    
    first_day = 0.5 # feet
    second_day = 8 / 12 # feet
    melted_snow = 2 / 12 # feet
    fifth_day = 2 * first_day # feet
    
    total_snow = first_day + second_day - melted_snow + fifth_day    
    result = total_snow
    
    return result

print(solution())