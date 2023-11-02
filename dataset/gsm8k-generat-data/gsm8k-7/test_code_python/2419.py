def solution():
    total_meat_needed = 210
    num_cubs = 4
    meat_per_cub_per_week = 35
    meat_per_bear_per_week = num_cubs * meat_per_cub_per_week
    meat_per_day = meat_per_bear_per_week / 7
    num_rabbits_per_day = meat_per_day / 5
    result = num_rabbits_per_day
    return result

print(solution())