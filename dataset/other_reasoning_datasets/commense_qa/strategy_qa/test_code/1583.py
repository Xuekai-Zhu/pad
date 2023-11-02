def solution():
    require_large_body_of_water = True
    no_indoor_pool_big_enough = True
    if require_large_body_of_water and no_indoor_pool_big_enough:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())