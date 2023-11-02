def solution():
    """Hannah wants to save $80 for five weeks. In the first week, she saved $4 and she plans to save twice as much as her savings as the previous week. How much will she save in the fifth week to reach her goal?"""
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