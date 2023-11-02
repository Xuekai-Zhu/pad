def solution():
    """While preparing balloons for Eva's birthday party, her mom bought 50 balloons and 1800cm³ of helium. One balloon needs 50cm³ to float high enough to touch the ceiling, and she can fill any remaining balloon with ordinary air. If she used up all of the helium and inflated every balloon, how many more balloons are touching the ceiling than not?"""
    
    # 50 balloons with 50cm³ helium each will use up all 1800cm³ helium
    num_helium_balloons = 1800 / 50
    
    # Calculate how many balloons can be filled with the remaining air
    num_air_balloons = 50 - num_helium_balloons
    
    # Calculate how many helium balloons will touch the ceiling
    num_touch_ceiling = num_helium_balloons
    
    # Calculate how many balloons will not touch the ceiling
    num_not_touch_ceiling = num_air_balloons
    
    # Calculate the difference between the two
    difference = num_touch_ceiling - num_not_touch_ceiling
    
    result = difference
    
    return result

print(solution())