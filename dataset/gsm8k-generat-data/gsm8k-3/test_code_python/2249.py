def solution():
    """At peak season, 6 packs of tuna fish are sold per hour, while in a low season 4 tuna packs are sold per hour. 
    If each tuna pack is sold at $60, how much more money is made in a day during a high season than a low season if the fish are sold for 15 hours?"""
    
    # calculate sales during peak season
    peak_sales = 6 * 15 * 60
    
    # calculate sales during low season
    low_sales = 4 * 15 * 60
    
    # calculate the difference in sales
    difference = peak_sales - low_sales
    
    # return the result
    return difference

print(solution())