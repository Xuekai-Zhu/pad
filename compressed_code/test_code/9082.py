def solution():
    
    goal = 80
    saved_week_1 = 4
    multipler = 2
    saved_week_2 = saved_week_1 * multipler
    saved_week_3 = saved_week_2 * multipler
    saved_week_4 = saved_week_3 * multipler
    saved_week_5 = goal - (saved_week_1 + saved_week_2 + saved_week_3 + saved_week_4)
    result = saved_week_5
    return result

print(solution())