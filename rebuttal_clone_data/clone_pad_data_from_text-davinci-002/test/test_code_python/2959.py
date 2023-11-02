def solution():
    caffeine_per_cup = 80
    goal = 200
    cups_drank = 3
    total_caffeine = caffeine_per_cup * cups_drank
    over_caffeine = total_caffeine - goal
    result = over_caffeine
    return result

print(solution())