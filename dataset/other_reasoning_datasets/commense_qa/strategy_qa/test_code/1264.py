def solution():
    dosa_calories = 110
    lumberjack_calories = 8000
    dosa_count = 3
    total_calories = dosa_calories * dosa_count
    if total_calories >= lumberjack_calories:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())