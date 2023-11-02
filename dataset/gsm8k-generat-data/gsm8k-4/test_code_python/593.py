def solution():
    """A big snowstorm caused a large amount of snow to fall onto Grandpa's farm, 
    and the wind caused the snow to pile up into a drift. But on the second day, 
    it warmed up enough that half of the snowdrift melted. The third day, it 
    snowed again, adding another 6 inches of snow onto the snowdrift. On the 
    fourth day, another 18 inches of snow fell onto the snowdrift. If the 
    snowdrift was 34 inches deep at the end of the fourth day, how deep in inches 
    was the drift at the end of the first day?"""
    
    # Start with the depth of the snowdrift on the fourth day
    depth_day4 = 34
    
    # Reverse the steps to find the depth of the snowdrift on the first day
    
    # On the fourth day, 18 inches were added
    depth_day3 = depth_day4 - 18
    
    # On the third day, 6 inches were added
    depth_day2 = depth_day3 - 6
    
    # On the second day, half of the snowdrift melted
    depth_day1 = depth_day2 * 2
    
    # The depth on the first day is the final answer
    result = depth_day1
    return result

print(solution())