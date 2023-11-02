def solution():
    """Four days ago, Carlos bought a bag of gummy worms. Every day he ate half of the remaining gummy worms. After eating half of the remainder on the fourth day, he now has 4 gummy worms left. How many gummy worms were in the bag when Carlos bought it?"""
    # Define the number of gummy worms left after the fourth day
    gummy_worms_left = 4
    
    # Backtrack to determine the number of gummy worms on the previous days
    gummy_worms_day_4 = gummy_worms_left * 2
    gummy_worms_day_3 = gummy_worms_day_4 * 2
    gummy_worms_day_2 = gummy_worms_day_3 * 2
    gummy_worms_day_1 = gummy_worms_day_2 * 2
    
    # Determine the initial number of gummy worms
    initial_gummy_worms = gummy_worms_day_1
    
    result = initial_gummy_worms
    return result

print(solution())