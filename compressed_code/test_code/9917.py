def solution():
    
    cakes_baked_per_day = 4
    days_baking = 6
    cakes_remaining = cakes_baked_per_day * days_baking
    for day in range(1, days_baking + 1):
        if day % 2 == 0:
            cakes_remaining -= 1
    return cakes_remaining

print(solution())