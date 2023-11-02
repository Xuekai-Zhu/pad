def solution():
    # Calculate Hannah's savings for each week
    week_1 = 4  
    week_2 = 2 * week_1  
    week_3 = 2 * week_2  
    week_4 = 2 * week_3  
    week_5 = (80 - week_1 - week_2 - week_3 - week_4)  # calculate the remaining amount needed to reach the goal

    result = week_5
    return result

print(solution())