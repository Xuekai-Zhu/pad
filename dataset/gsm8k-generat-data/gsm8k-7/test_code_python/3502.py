def solution():
    morning_crickets = 5
    afternoon_crickets = 3 * morning_crickets
    total_crickets_per_day = morning_crickets + (afternoon_crickets * 2)

    result = total_crickets_per_day
    return result

print(solution())