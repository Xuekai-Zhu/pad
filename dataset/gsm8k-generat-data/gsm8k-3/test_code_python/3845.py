def solution():
    """During a recent three-day trip to Italy, Keziah and her mom went mushroom picking.
    They sold all the mushrooms they picked on the first day for a total of $58.
    The day after, they picked 12 mushrooms. On the last day, they picked double the mushrooms they had picked the previous day.
    If the price per mushroom was $2, what is the total number of mushrooms they picked?"""
    
    # Calculate the total amount earned on day 1
    day1_earnings = 58
    
    # Calculate the number of mushrooms picked on day 2
    day2_mushrooms = 12
    
    # Calculate the number of mushrooms picked on day 3
    day3_mushrooms = day2_mushrooms * 2
    
    # Calculate the total number of mushrooms picked
    total_mushrooms = day2_mushrooms + day3_mushrooms
    
    # Calculate the total earnings from all mushrooms
    total_earnings = (total_mushrooms + 12) * 2
    
    result = total_mushrooms
    return result

print(solution())