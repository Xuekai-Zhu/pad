def solution():
    bees_hatched_per_day = 3000
    bees_lost_per_day = 900
    initial_bee_count = 12500
    total_bee_count = initial_bee_count + (bees_hatched_per_day - bees_lost_per_day) * 7
    result = total_bee_count
    return result

print(solution())