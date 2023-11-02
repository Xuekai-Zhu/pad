def solution():
    screens_march = 8800
    
    # Calculate how many screens Bennett sold in February and January combined
    screens_feb = screens_march / 4
    screens_jan = screens_feb / 2
    total_screens = screens_march + screens_feb + screens_jan
    
    result = total_screens
    return result

print(solution())