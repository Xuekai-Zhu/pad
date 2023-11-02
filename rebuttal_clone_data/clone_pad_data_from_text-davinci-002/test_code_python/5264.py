def solution():
    cakes_baked_per_day = 4
    days = 6
    cakes_eaten_by_brother = 3
    total_cakes_baked = cakes_baked_per_day * days
    total_cakes_eaten = cakes_eaten_by_brother * days
    remaining_cakes = total_cakes_baked - total_cakes_eaten
    result = remaining_cakes
    return result

print(solution())