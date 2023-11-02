def solution():
    
    initial_roses = 2 * 12 + 1 * 12  
    wilted_roses_day1 = initial_roses // 2
    remaining_roses_day1 = initial_roses - wilted_roses_day1
    wilted_roses_day2 = remaining_roses_day1 // 2
    remaining_roses_day2 = remaining_roses_day1 - wilted_roses_day2
    unwilted_roses = remaining_roses_day2
    result = unwilted_roses
    
    return result

print(solution())