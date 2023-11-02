def solution():
    """Kimberly loves gumballs and will trade almost anything she owns for them. A friend knows that Kim has a 
    bunch of shiny new earrings that she loves. She agrees to give Kim 9 gumballs for each pair of earrings.
    On the first day, Kim brings her 3 pairs of earrings. On the second she brings her twice as many.
    On the third day, she brings 1 less than she brought on the second day. 
    If Kim eats 3 gumballs a day, how many days will the gumballs last?"""
    
    # Calculate the number of earrings Kim brings each day
    earrings_day1 = 3
    earrings_day2 = 2 * earrings_day1
    earrings_day3 = earrings_day2 - 1
    
    # Calculate the number of gumballs Kim receives each day 
    gumballs_day1 = 9 * earrings_day1
    gumballs_day2 = 9 * earrings_day2
    gumballs_day3 = 9 * earrings_day3
    
    # Calculate total number of gumballs Kim receives 
    total_gumballs = gumballs_day1 + gumballs_day2 + gumballs_day3
    
    # Calculate number of days the gumballs will last 
    gumballs_per_day = 3
    days = total_gumballs // gumballs_per_day
    
    result = days
    return result

print(solution())