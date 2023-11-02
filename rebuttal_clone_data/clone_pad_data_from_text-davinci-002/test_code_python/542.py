def solution():
    cakes_baked = 10
    days_baked = 5
    cakes_eaten = 12
    cakes_remaining = cakes_baked * days_baked - cakes_eaten
    cans_of_frosting = 2
    result = cans_of_frosting * cakes_remaining
    return result

print(solution())