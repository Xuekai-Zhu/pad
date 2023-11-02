def solution():
    caffeine_per_cup = 80
    max_caffeine_per_day = 200
    num_cups = 3

    # Calculate the total caffeine Lisa consumed from her three cups of coffee
    total_caffeine = num_cups * caffeine_per_cup

    # Calculate how much caffeine Lisa went over her daily limit
    excess_caffeine = max(total_caffeine - max_caffeine_per_day, 0)

    result = excess_caffeine
    return result

print(solution())