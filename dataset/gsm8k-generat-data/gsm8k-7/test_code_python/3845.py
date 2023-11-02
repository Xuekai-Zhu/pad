def solution():
    mushrooms_day1 = ?? # unknown value
    mushrooms_day2 = 12
    mushrooms_day3 = mushrooms_day2 * 2
    
    total_mushrooms = mushrooms_day1 + mushrooms_day2 + mushrooms_day3
    
    total_earnings = mushrooms_day1 * 2 + mushrooms_day2 * 2 + mushrooms_day3 * 2
    
    # We know that total_earnings = $58 on day 1
    # Therefore, mushrooms_day1 * 2 = $58
    mushrooms_day1 = 29
    
    result = total_mushrooms
    return result

print(solution())