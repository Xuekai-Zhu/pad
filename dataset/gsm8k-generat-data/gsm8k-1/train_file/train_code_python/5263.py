def solution():
    """In preparation for the church fundraiser, Julia bakes one less than 5 cakes per day for 6 days. Unfortunately, every other day, Julia's brother, Clifford, sneaks into Julia's house and eats one of Julia's cakes. At the end of 6 days, how many cakes does Julia have remaining?"""
    cakes_baked_per_day = 4
    days_baking = 6
    cakes_remaining = cakes_baked_per_day * days_baking
    for day in range(1, days_baking + 1):
        if day % 2 == 0:
            cakes_remaining -= 1
    return cakes_remaining

print(solution())