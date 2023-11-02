def solution():
    """In preparation for the church fundraiser, Julia bakes one less than 5 cakes per day for 6 days. Unfortunately, every other day, Julia's brother, Clifford, sneaks into Julia's house and eats one of Julia's cakes. At the end of 6 days, how many cakes does Julia have remaining?"""
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