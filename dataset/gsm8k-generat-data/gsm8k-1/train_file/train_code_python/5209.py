def solution():
    """There is 80 mg of caffeine in a cup of coffee. Lisa does not want to drink more than 200 mg of caffeine per day. If she drinks three cups of coffee, how many milligrams of coffee did Lisa drink over her goal?"""
    caffeine_per_cup = 80
    max_caffeine_per_day = 200
    cups_consumed = 3
    total_caffeine_consumed = caffeine_per_cup * cups_consumed
    caffeine_over_goal = total_caffeine_consumed - max_caffeine_per_day
    result = caffeine_over_goal
    return result

print(solution())