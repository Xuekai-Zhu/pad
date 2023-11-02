def solution():
    """Last night Kannon had 3 apples, a banana, and 4 oranges for dinner. Today she is planning to have 4 more apples than last night, 10 times as many bananas as she ate last night, and twice as many oranges as apples she'll have today. How many fruits would she have eaten so far in the two meals?"""
    apples_last_night = 3
    bananas_last_night = 1
    oranges_last_night = 4
    apples_today = apples_last_night + 4
    bananas_today = bananas_last_night * 10
    oranges_today = apples_today * 2
    total_fruits_eaten = apples_last_night + bananas_last_night + oranges_last_night + apples_today + bananas_today + oranges_today
    result = total_fruits_eaten
    
    return result

print(solution())