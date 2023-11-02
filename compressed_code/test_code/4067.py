def solution():
    
    cakes_baked_per_day = 4
    total_days = 6
    cakes_remaining = 0
    for i in range(1, total_days + 1):
        if i % 2 == 0:
            cakes_baked = cakes_baked_per_day - 1
        else:
            cakes_baked = cakes_baked_per_day
        cakes_remaining += cakes_baked
    result = cakes_remaining
    return result

print(solution())