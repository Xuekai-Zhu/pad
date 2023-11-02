def solution():
    """Magdalena has an apple tree on their farm, producing very few apples each year for a while now. However, this year, the apple tree yield was excellent, and it grew 200 apples. Magdalena picked 1/5 of the fruits on the first day, twice that number on the second day, and 20 more apples than he picked on the first day on the third day. Calculate the total number of apples remaining in the tree."""
    total_apples = 200
    first_day_pick = total_apples / 5
    second_day_pick = 2 * first_day_pick
    third_day_pick = first_day_pick + 20
    
    total_picked = first_day_pick + second_day_pick + third_day_pick
    apples_remaining = total_apples - total_picked
    
    return apples_remaining

print(solution())