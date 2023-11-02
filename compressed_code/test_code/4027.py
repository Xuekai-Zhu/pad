def solution():
    
    caffeine_per_cup = 80
    max_caffeine_per_day = 200
    total_caffeine = caffeine_per_cup * 3
    over_goal = max(total_caffeine - max_caffeine_per_day, 0)
    result = over_goal
    return result

print(solution())