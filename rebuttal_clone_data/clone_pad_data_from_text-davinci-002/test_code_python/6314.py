def solution():
    total_peaches = 18
    ripe_peaches = 4
    unripe_peaches = total_peaches - ripe_peaches
    peaches_ripe_per_day = 2
    peaches_eaten_per_day = 3
    ripe_peaches_5_days = ripe_peaches + (peaches_ripe_per_day * 5) - (peaches_eaten_per_day * 2)
    unripe_peaches_5_days = unripe_peaches + (peaches_ripe_per_day * 2)
    difference = ripe_peaches_5_days - unripe_peaches_5_days
    result = difference
    return result

print(solution())