def solution():
    
    total_cakes = 60
    cakes_already_baked = total_cakes / 2
    cakes_left_to_bake = total_cakes - cakes_already_baked
    cakes_baked_today = cakes_left_to_bake / 2
    cakes_left_to_bake = cakes_left_to_bake - cakes_baked_today
    cakes_baked_tomorrow = cakes_left_to_bake / 3
    total_cakes_baked = cakes_already_baked + cakes_baked_today + cakes_baked_tomorrow
    cakes_left_to_bake = total_cakes - total_cakes_baked
    result = cakes_left_to_bake
    return result

print(solution())