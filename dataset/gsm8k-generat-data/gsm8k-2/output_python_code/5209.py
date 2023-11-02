def solution():
    """There is 80 mg of caffeine in a cup of coffee. Lisa does not want to drink more than 200 mg of caffeine per day. If she drinks three cups of coffee, how many milligrams of coffee did Lisa drink over her goal?"""
    caffeine_per_cup = 80
    max_caffeine_per_day = 200
    total_caffeine = caffeine_per_cup * 3
    over_goal = max(total_caffeine - max_caffeine_per_day, 0)
    result = over_goal
    return result

print(solution())