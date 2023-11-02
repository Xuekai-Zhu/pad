def solution():
    """A bowl of fruit holds 18 peaches. Four of the peaches are ripe and two more ripen every day, but on the third day three are eaten. How many more ripe peaches than unripe peaches are in the bowl after five days?"""
    
    # Define the initial number of ripe and unripe peaches
    initial_ripe = 4
    initial_unripe = 18 - initial_ripe
    
    # Simulate the peaches ripening over 5 days
    for day in range(1, 6):
        # Ripen 2 more peaches
        ripe_today = 2
        
        # On the third day, 3 peaches are eaten
        if day == 3:
            ripe_today -= 3
        
        # Add the new ripe peaches to the total
        initial_ripe += ripe_today
        
        # Subtract the new ripe peaches from the unripe peaches
        initial_unripe -= ripe_today
        
    # Calculate the difference between the ripe and unripe peaches
    difference = initial_ripe - initial_unripe
    
    # return the result
    result = difference
    return result

print(solution())